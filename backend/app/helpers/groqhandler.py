import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqHandler:
    def __init__(self):
        self.groq_client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

    chat_example = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content" : "Summarize the most significant news headlines in the last 24 hours.",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return {"Message": chat_example.choices[0].message.content}