# @ Author: Bertan Berker
# @Language: Python 3.11
# This file contains functions that prepare the SQL dataset and process the kaggle dataset
#
#

import base64
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
dataset_path = os.environ.get("DATASET_PATH")

client = OpenAI()


def process_image(image_path):

    image_path = image_path
    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    # Getting the Base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in this image? Describe in detail but do it in 50 words or less",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content



# This function iterates over the downloaded Kaggle folder
# and returns a list of image files
def process_kaggle():

    # Get all files inside the dataset path (including subdirectories)
    file_list = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file[len(file)-3:] == "jpg":
                file_list.append(os.path.join(root, file))

    return file_list



def prepare_sql_database():

    file_list = process_kaggle()

    try:
        for image_path in file_list:
            description = process_image(image_path)

            # ADD the description and the image URL to SQL database

    except:
        print("Error occured while trying to process images...")

    finally:
        print("Image processing is completed. Check your SQL...")



    


