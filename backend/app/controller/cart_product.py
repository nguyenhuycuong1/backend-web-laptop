from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from typing import List
from app.model.cart_product import CartProduct
from app.config import db, commit_rollback
from app.schema.cart_product import CartProductRequest, CartProductResponse
from sqlalchemy.future import select
from app.model.cart_product import CartProduct

router = APIRouter(prefix="", tags=["Cart Product"])



# @router.post("/addtocart")
# async def addtocart(cartproduct_data: CartProductRequest):
#     cartproduct = CartProduct(**cartproduct_data.dict())
#     db.session.add(cartproduct)
#     await commit_rollback()
#     await db.session.refresh(cartproduct)
#     return {"message": "Add to cart successfully"}

@router.post("/addtocart")
async def addtocart(cartproduct_data: CartProductRequest):
    cartproduct = CartProduct(**cartproduct_data.dict())

    existing_cartproduct = await check_existing_cart_product(cartproduct.cart_id, cartproduct.product_id)
    if existing_cartproduct:
        existing_cartproduct.quantity += cartproduct.quantity
        await commit_rollback()
        await db.session.refresh(existing_cartproduct)
        return {"message": "Quantity updated successfully"}

    db.session.add(cartproduct)
    await commit_rollback()
    await db.session.refresh(cartproduct)
    return {"message": "Added to cart successfully"}

@router.get("/carts", response_model=List[CartProductResponse])
async def carts():
    query = select(CartProduct)
    result = await db.session.execute(query)
    carts = result.scalars().all()
    return carts


async def check_existing_cart_product(cart_id: int, product_id: int):
    query = select(CartProduct).filter(
        CartProduct.cart_id == cart_id,
        CartProduct.product_id == product_id
    )
    result = await db.session.execute(query)
    return result.scalar_one_or_none()