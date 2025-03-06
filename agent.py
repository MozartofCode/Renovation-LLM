# @ Author: Bertan Berker
# @ Language: Python 3.11
#
#
#


import os
from dotenv import load_dotenv
from openai import OpenAI

openai_api_key = os.getenv('OPENAI_API_KEY')
load_dotenv()
client = OpenAI()


def gpt_call(prompt):

    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    message_content = completion.choices[0].message.content
    return message_content


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


print(generate_image("A white cat"))






