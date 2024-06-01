import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(".env.local")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_gpt_response(prompt):
    """OpenAI Chat Completion"""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content.strip()