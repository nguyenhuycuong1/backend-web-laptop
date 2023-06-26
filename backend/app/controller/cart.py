from fastapi import APIRouter, HTTPException
from fastapi import APIRouter
from sqlalchemy.future import select
from typing import List
from app.model.cart import Cart
from app.config import db
from app.schema.cart import CartResponse

router = APIRouter(prefix="", tags=["Cart"])


@router.get("/cart", response_model=List[CartResponse])
async def cart():
    query = select(Cart)
    result = await db.session.execute(query)
    cart = result.scalars().all()
    return cart
