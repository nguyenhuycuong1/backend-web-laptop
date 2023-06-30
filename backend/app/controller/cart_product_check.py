from fastapi import APIRouter, Depends, Security, HTTPException, Path, Query
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import or_
from sqlalchemy.sql import func
from typing import List
from app.model.cart_product_check import CartProductCheck
from app.config import db, commit_rollback
from app.schema.cart_product_check import (
    CartProductRequest,
    CartProductResponse
)

router = APIRouter(prefix="", tags=["CartProductCheck"])


@router.post("/cart_product_check", response_model=CartProductResponse)
async def create_product(product_data: CartProductRequest):
    cart_product_check = CartProductCheck(**product_data.dict())
    db.session.add(cart_product_check)
    await commit_rollback()
    await db.session.refresh(cart_product_check)
    return cart_product_check
