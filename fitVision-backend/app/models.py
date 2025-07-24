from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str]  # MongoDB _id as string
    name: str
    category: str
    image: str
    modelUrl: str
    rating: float
    triedCount: int
