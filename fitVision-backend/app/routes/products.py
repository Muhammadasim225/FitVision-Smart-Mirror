from fastapi import APIRouter
from app.database import product_collection
from fastapi import HTTPException
from bson import ObjectId
router = APIRouter()

@router.get("/products/{category}")
async def get_products_by_category(category: str):
    products = list(product_collection.find({"category": category}))
    for p in products:
        p["_id"] = str(p["_id"])
    return products



@router.get("/product/{product_id}")
async def get_product_by_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID format")

    product = product_collection.find_one({"_id": ObjectId(product_id)})

    if product:
        product["_id"] = str(product["_id"]) 
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")
