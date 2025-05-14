from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(
    title="Workshop API",
    description="A demo API for GitHub CI/CD workshop",
    version="0.1.0",
)

# In-memory database to store items
db = []


class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None


class ItemResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Workshop API Dectech! Go to /docs for the API documentation."}


@app.get("/items", response_model=List[ItemResponse])
async def get_items():
    """
    Get all items from the database
    """
    return db


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    """
    Create a new item in the database
    """
    item_dict = item.dict()
    item_dict["id"] = str(uuid.uuid4())
    db.append(item_dict)
    return item_dict


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    """
    Get a specific item by ID
    """
    for item in db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.on_event("startup")
async def startup_event():
    # Add some initial items
    db.append({"id": str(uuid.uuid4()), "name": "Item 1", "description": "This is the first item"})
    db.append({"id": str(uuid.uuid4()), "name": "Item 2", "description": "This is the second item"}) 