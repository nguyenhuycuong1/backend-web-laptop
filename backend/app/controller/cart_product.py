from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from typing import List
from app.model.cart_product import CartProduct
from app.config import db, commit_rollback
from app.schema.cart_product import CartProductCreateRequest, CartProductResponse

router = APIRouter(prefix="", tags=["Cart Product"])

@router.post("/addtocart", response_model=CartProductResponse)
async def addtocart(cartproduct_data: CartProductCreateRequest):
    cartproduct = CartProduct(**cartproduct_data.dict())
    db.session.add(cartproduct)
    await commit_rollback()
    await db.session.refresh(cartproduct)
    return cartproduct

@router.get("/carts", response_model=List[CartProductResponse])
async def carts():
    query = select(CartProduct)
    result = await db.session.execute(query)
    carts = result.scalars().all()
    return carts