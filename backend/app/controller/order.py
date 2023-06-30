from fastapi import APIRouter
from app.model.order import Order
from app.config import db, commit_rollback
from app.schema.order import (
    OrderBase,
    OrderRequest,
    OrderResponse,
    ResponseSchema
)

router = APIRouter(prefix="", tags=["Order"])

@router.post("/order", response_model=ResponseSchema)
async def create_order(product_data: OrderRequest):
    order = Order(**product_data.dict())
    db.session.add(order)
    await commit_rollback()
    await db.session.refresh(order)
    return ResponseSchema(detail="Successfully fetch order!")