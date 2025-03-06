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

def gpt_call(role, prompt):

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": role, "content": prompt}
        ]
    )

    message_content = completion.choices[0].message.content
    return message_content










