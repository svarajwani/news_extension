import os
import json
from typing import Union
from fastapi import FastAPI, Request
from groq import Groq
from app.helpers.newshandler import NewsHandler

app = FastAPI()


@app.get("/articles")
async def read_root():
    articles = NewsHandler().get_articles()
    client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

    chat_example = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a detail-oriented AI assistant. You excel at providing responses strictly in valid JSON if requested. When asked for a JSON response, you must output valid JSON with no additional commentary, whitespace, or other text outside of the JSON structure."
            },
            {
                "role": "user",
                "content" : f"Choose the most significant news headlines in this JSON dataset: {articles} "
                            "and give me a JSON-formatted response list with all the chosen significant articles. "
                            "Please return the final result as valid JSON in this format: "
                            '{"significant_news_headlines": ['
                            '{"title": "...", "description": "...", "url": "..."}, ...]}'
            },
        ],
        model="llama-3.3-70b-versatile",
        response_format={ "type": "json_object" },
        frequency_penalty=-2.0,
    )

    return chat_example.choices[0].message.content


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}