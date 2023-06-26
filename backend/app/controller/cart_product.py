from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from typing import List
from app.model.cart_product import CartProduct
from app.config import db, commit_rollback
from app.schema.cart_product import CartProductCreateRequest, CartProductResponse

router = APIRouter(prefix="", tags=["Cart Product"])

@router.post("/cartproduct", response_model=CartProductResponse)
async def create_product(cartproduct_data: CartProductCreateRequest):
    cartproduct = CartProduct(**cartproduct_data.dict())
    db.session.add(cartproduct)
    await commit_rollback()
    await db.session.refresh(cartproduct)
    return cartproduct
