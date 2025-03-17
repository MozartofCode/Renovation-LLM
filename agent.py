# @ Author: Bertan Berker
# @ Language: Python 3.11
# This file contains the functions for making the API calls to the OpenAI API
# and generating the renovated image

import os
from dotenv import load_dotenv
from openai import OpenAI
import psycopg2 
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
dataset_path = os.getenv("DATASET_PATH")
postgres_password = os.getenv("POSTGRES_PASSWORD")

client = OpenAI()


# This function makes the API call to the OpenAI API
# :param image_descriptions: A list of image descriptions of possible designs
# :param user_prompt: The prompt from the user
# :return: A complete description of the image to be generated
def generate_description(image_descriptions, user_prompt):
    
    background = f"You are a professional interior designer. You are given a list of image descriptions: [{image_descriptions}] of possible designs \
        and a user prompt: {user_prompt}. \
        You need to generate a complete description of the image to be generated."
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": background}
        ]
    )

    description = completion.choices[0].message.content
    return description


# This function generates the image
# :param prompt: The prompt from the user
# :return: The generated image  
def generate_image(prompt):

    response = client.images.generate(
    model="dall-e-3",
    prompt= prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
    print(response)
    return response.data[0].url


# This function analyzes the user prompt and extracts requirements
# related to room type, price range, color preferences, and design style
# :param user_prompt: The prompt from the user containing design requirements
# :return: A list of extracted requirements for SQL query generation
def analyze_requirements(user_prompt):
    
    background = f"You are a professional interior designer. You are given a user prompt: {user_prompt}. \
        You need to analyze the prompt and extract the requirements related to room type, price range, color preferences, and design style. \
        You need to return the requirements in the form of a list of strings. \
        The requirements should be related to the room type, price range, color preferences, and design style. \
        For example: ['Room type is Kitchen', 'Price range is $1000-$2000', 'Color preferences are blue and white', 'Design style is modern']"
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": background}
        ]
    )

    requirements = completion.choices[0].message.content
    return requirements


# This function generates the SQL commands based on analyzing the prompt
# on the room type, price, color, and style
# :param requirements: A lsit of requirements from the user
# :return: A list of SQL commands
def generate_sql_commands(requirements):
        
    background = f"You are a professional software engineer who is main job is writing SQL commands to get information from a database \
        You are given a bunch of requirements: [{requirements}] and you are given the task to return a list of SQL commands \
        that can be used to get the information from the database based on these requirements. The commands should be in the form of a SELECT statement. \
        Additionally, get information that satisfies one or more of the requirements. I want you to return the 'image_description' column of the results. \
            For example: SELECT image_description FROM renovation_photos WHERE room_type = 'Kitchen' AND price = 1000 AND color = 'blue' AND style = 'modern' etc."

    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": background}
        ]
    )

    sql_commands = completion.choices[0].message.content
    return sql_commands


# This function runs the SQL commands and returns the results
# :param sql_commands: A list of SQL commands
# :return: A list of image descriptions from the SQL database
def run_sql_commands(sql_commands):

    conn = psycopg2.connect(
        dbname="renovation_db",
        user="postgres",
        password=postgres_password,
        host="localhost",
        port="5000"  
    )

    cursor = conn.cursor()

    descriptions = []
    
    try:
        for command in sql_commands:
            cursor.execute(command)
            results = cursor.fetchall()
            print(f"Results for command: {command}")
            descriptions.append(results)

    except Exception as e:
        print(f"Fatal error in database operation: {str(e)}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

    return descriptions