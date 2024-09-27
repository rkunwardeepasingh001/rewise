from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from app.api.v1.endpoints import items,users

app = FastAPI()

app.include_router(items.router,prefix="/items",tags=["items"])
app.include_router(users.router,prefix="/users",tags=["users"])

@app.get("/")
def read_root():
    return {"message":"Welcome to the fast api project"}
