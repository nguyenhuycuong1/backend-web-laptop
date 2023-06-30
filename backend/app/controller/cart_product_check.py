from fastapi import APIRouter, Depends, Security, HTTPException, Path, Query
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import or_
from sqlalchemy.sql import func
from typing import List
from app.model.cart_product_check import CartProductCheck
from app.config import db, commit_rollback
from app.schema.cart_product_check import (
    CartProductCheckRequest,
    CartProductCheckResponse,
    CartProductCheckItemResponse
)

router = APIRouter(prefix="", tags=["CartProductCheck"])


@router.post("/cart_product_check", response_model=CartProductCheckResponse)
async def create_cart_product_check(product_data: CartProductCheckRequest):
    cart_product_check = CartProductCheck(**product_data.dict())
    db.session.add(cart_product_check)
    await commit_rollback()
    await db.session.refresh(cart_product_check)
    return cart_product_check

@router.get("/cart_product_check/{cart_product_check_id}", response_model=CartProductCheckItemResponse)
async def get_cart_product_check(cart_product_check_id: str):
    query = select(CartProductCheck).where(CartProductCheck.cart_product_check_id == cart_product_check_id)
    result = await db.session.execute(query)
    cart_product_check = result.scalars().first()
    if not cart_product_check:
        raise HTTPException(status_code=404, detail="Cart Product Check not found")
    return cart_product_check