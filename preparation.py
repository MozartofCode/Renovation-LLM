# @ Author: Bertan Berker
# @Language: Python 3.11
# This file contains functions that prepare the SQL dataset and process the kaggle dataset
#
#

import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

openai_api_key = os.getenv('OPENAI_API_KEY')
dataset_path = os.getenv("DATASET_PATH")
load_dotenv()

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

