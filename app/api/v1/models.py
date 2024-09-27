from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class FirstItem(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

