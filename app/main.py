from typing import Optional, Union
from fastapi import FastAPI, Query
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Union[str, None] = None
  price: float
  tax: Union[float, None] = None

app = FastAPI()

items = [
  {
    "item_id": 1,
    "name": ""
  }
]

@app.get("/")
async def root():
  return {"message":"Hello"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(default = None, max_length = 50)):
  results = { "items": [{"item_id": "Foo"}, {"item_id": "Bar"}] }

  if q:
    results.update({"q": q})
  return results

@app.get("/users/{user_id}")
def read_user_me(user_id: str):
  return {"user_id": user_id}

@app.post("/items/")
def read_items(item: Item):
  item_dict = item.dict()
  
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with_tax": price_with_tax})

  return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
  result = {"item_id": item_id, **item.dict()}
  if q:
    result.update({"q": q})
  return result