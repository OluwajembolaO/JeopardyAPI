# this file contains all the AI related functions for jeapordy.py
from openai import AzureOpenAI
from secret import *

#Setting up AI
AOAI_ENDPOINT = AZURE_OPENAI_ENDPOINT
AOAI_KEY = AZURE_OPENAI_API_KEY 
MODEL_NAME = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version="2024-05-01-preview",
)

def jeapordyOpenAI(prompt):
    response = openai_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000
            )
    ai_response = (response.choices[0].message.content)

    return ai_response

