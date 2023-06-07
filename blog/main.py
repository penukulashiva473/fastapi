from typing import Union
from fastapi import FastAPI

from blog.schemas import Item


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    return item