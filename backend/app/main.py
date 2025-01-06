import os
import json
from typing import Union
from fastapi import FastAPI, Request
from app.helpers.newshandler import NewsHandler
import sys
print("Python Path:", sys.path)

app = FastAPI()


@app.post("/")
async def read_root():
    # articles = NewsHandler().get_articles()a
    # return articles
    return 0


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}