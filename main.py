import openai
import os

openai.api_key = os.getenv('')

def get_response(prompt):
    response = openai.completion.create(
        engine="text-"
    )