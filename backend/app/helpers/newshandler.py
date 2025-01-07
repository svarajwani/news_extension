import requests
import os
import json
from dotenv import load_dotenv
from newsapi import NewsApiClient


class NewsHandler:
    def __init__(self):
        load_dotenv()
        key=os.getenv("NEWS_API_KEY")
        if not key:
             raise ValueError("Missing NEWS_API_KEY in environment variables")
        self.newsapi = NewsApiClient(api_key=key)

    def get_articles(self):
        #top_headlines = self.newsapi.get_top_headlines(language='en', country='us')
        top_headlines = self.newsapi.get_top_headlines(
                                          language='en',
                                          country='us')
        return top_headlines

    def clean_articles(self, articles):
        cleaned = []
        for article in articles:
            if all(k in article and article[k] for k in ["title", "description", "url"]):
                newarticle = {
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"]
                }
                cleaned.append(newarticle)

        return cleaned