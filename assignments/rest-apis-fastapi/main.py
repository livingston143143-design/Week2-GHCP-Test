from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# In-memory storage
items: dict[int, Item] = {}
next_id = 1

@app.get("/items/")
def read_items():
    return list(items.values())

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@app.post("/items/", status_code=201)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    next_id += 1
    return item

# To run: uvicorn main:app --reload
