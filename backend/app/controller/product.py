from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from typing import List
from app.model.product import Product
from app.config import db, commit_rollback
from app.schema.product import ProductCreateRequest, ProductItemResponse, ProductUpdateRequest, ProductListResponse

router = APIRouter(prefix="", tags=["Product"])

@router.post("/product", response_model=ProductItemResponse)
async def create_product(product_data: ProductCreateRequest):
    product = Product(**product_data.dict())
    db.session.add(product)
    await commit_rollback()
    await db.session.refresh(product)
    return product

@router.get("/product/{product_id}", response_model=ProductItemResponse)
async def get_product(product_id: str):
    query = select(Product).where(Product.product_id == product_id)
    result = await db.session.execute(query)
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/products", response_model=List[ProductListResponse])
async def list_products():
    query = select(Product)
    result = await db.session.execute(query)
    products = result.scalars().all()
    return products

@router.put("/product/{product_id}", response_model=ProductItemResponse)
async def update_product(product_id: str, product_data: ProductUpdateRequest):
    query = select(Product).where(Product.product_id == product_id)
    result = await db.session.execute(query)
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in product_data.dict().items():
        setattr(product, field, value)
    await commit_rollback()
    await db.session.refresh(product)
    return product

@router.delete("/product/{product_id}")
async def delete_product(product_id: str):
    query = select(Product).where(Product.product_id == product_id)
    result = await db.session.execute(query)
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.session.delete(product)
    await commit_rollback()
    return {"message": "Product deleted successfully"}

@router.get("/products/orderby/{options}", response_model=List[ProductListResponse])
async def List_products_orderBy(options: str):
    if(options == "desc"):
        query = select(Product).order_by(Product.price.desc())    
    elif(options == "asc"):
        query = select(Product).order_by(Product.price.asc())            
    result = await db.session.execute(query)
    products = result.scalars().all()
    return products