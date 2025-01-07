import os
import json

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from groq import Groq
from app.helpers.newshandler import NewsHandler

app = FastAPI()

origins = [
    "http://127.0.0.1.8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/articles")
def read_root():
    articles = NewsHandler().get_articles()
    articlesList = articles["articles"]
    cleanedArticles = NewsHandler().clean_articles(articlesList)
    client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

    chat_example = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a detail-oriented AI assistant."
            },
            {
                "role": "user",
                "content" : f"Choose the most significant news headlines in this JSON dataset: {cleanedArticles} "
                            "and give me a JSON-formatted response list with all the chosen significant articles. "
                            "Please return the final result in this format: "
                            '{"significant_news_headlines": ['
                            '{"title": "...", "description": "...", "url": "..."}, ...]}'
            },
        ],
        model="gemma2-9b-it",
        response_format={ "type": "json_object" },
        frequency_penalty=-2.0,
        )

    res = chat_example.choices[0].message.content
    return res