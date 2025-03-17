# @ Author: Bertan Berker
# @Language: Python 3.11
# This file contains functions that prepare the SQL dataset and process the kaggle dataset

import base64
from openai import OpenAI
import os
from dotenv import load_dotenv
import psycopg2
import json
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
dataset_path = os.environ.get("DATASET_PATH")
postgres_password = os.environ.get("POSTGRES_PASSWORD")

client = OpenAI()

from pydantic import BaseModel
from typing import List

class ImageAnalysis(BaseModel):
    image_description: str
    room_type: str 
    price: int
    color: str
    style: str

# This function processes the design image and returns the description
# :param image_path: The path to the image file
# :return: ImageAnalysis object containing structured image details
def process_image(image_path):

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    try:
        # Getting the Base64 string
        base64_image = encode_image(image_path)

        background = """You are a professional interior designer. Analyze this room image and return ONLY a JSON object with these exact fields:
        {
            "image_description": "brief description under 50 words",
            "room_type": "type of room",
            "price": "price in integer form",
            "color": "main color used",
            "style": "design style"
        }
        Return ONLY valid JSON, no other text."""
        
        print(f"Processing image: {image_path}")
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {
                    "role": "user", 
                    "content": [
                        {
                            "type": "text",
                            "text": background,
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }
            ],
        )

        raw_content = response.choices[0].message.content
        print(f"Raw GPT response: {raw_content}")
        
        # Clean up the response by removing markdown code block markers
        cleaned_content = raw_content.replace("```json", "").replace("```", "").strip()
        print(f"Cleaned content: {cleaned_content}")
        
        analysis_dict = json.loads(cleaned_content)
        print(f"Parsed JSON: {analysis_dict}")
        
        return ImageAnalysis(**analysis_dict)

    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        raise  # Re-raise the exception to be caught by the main try-catch block


# This function iterates over the downloaded Kaggle folder
# and returns a list of image files
# :return: A list of image files
def process_kaggle():

    # Get all files inside the dataset path (including subdirectories)
    file_list = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file[len(file)-3:] == "jpg":
                file_list.append(os.path.join(root, file))

    return file_list


# This function prepares the SQL database
# :return: None
def prepare_sql_database():
    # Database connection parameters
    conn = psycopg2.connect(
        dbname="renovation_db",
        user="postgres",
        password=postgres_password,
        host="localhost",
        port="5000"  # Changed to default PostgreSQL port
    )

    cursor = conn.cursor()
    
    file_list = process_kaggle()
    print(f"Found {len(file_list)} images to process")

    try:
        for idx, image_path in enumerate(file_list):
            try:
                print(f"\nProcessing image {idx + 1}/{len(file_list)}: {image_path}")
                processed_information = process_image(image_path)
                
                # Convert color list to string for database storage
                color_str = ', '.join(processed_information.color)
                
                # Insert query with placeholders for all columns
                insert_query = """
                    INSERT INTO renovation_photos (image_url, image_description, room_type, price, color, style)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                
                values = (
                    image_path,          
                    processed_information.image_description,          
                    processed_information.room_type,               
                    processed_information.price,               
                    color_str,               
                    processed_information.style                
                )
                
                cursor.execute(insert_query, values)
                conn.commit()
                print(f"Successfully inserted data for {image_path}")

            except Exception as e:
                print(f"Error processing individual image {image_path}: {str(e)}")
                continue  # Skip to next image on error

    except Exception as e:
        print(f"Fatal error in database operation: {str(e)}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        print("Image processing is completed. Check your SQL database...")


if __name__ == "__main__":
    prepare_sql_database()
