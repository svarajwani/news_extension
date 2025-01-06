import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient

class NewsHandler:
    def __init__(self):
        api_key=os.getenv("NEWS_API_KEY")
        print(api_key)
        if not api_key:
            raise ValueError("Missing NEWS_API_KEY in environment variables")
        self.newsapi = NewsApiClient(api_key)

    def get_articles(self):
        #top_headlines = self.newsapi.get_top_headlines(language='en', country='us')
        top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

        return top_headlines