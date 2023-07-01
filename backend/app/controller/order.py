from fastapi import APIRouter
from app.model.order import Order
from app.config import db, commit_rollback
from typing import List
from app.schema.order import OrderBase, OrderRequest, OrderResponse, ResponseSchema
import uuid

router = APIRouter(prefix="", tags=["Order"])


@router.post("/order", response_model=List[OrderResponse])
async def create_order(product_data: List[OrderRequest]):
    order_id = str(uuid.uuid4())  # Tạo order_id mới

    orders = []
    for data in product_data:
        order = Order(
            order_id=order_id, **data.dict()
        )  # Gán cùng order_id cho tất cả các đối tượng Order
        orders.append(order)

    db.session.add_all(orders)
    await commit_rollback()
    for order in orders:
        await db.session.refresh(order)

    return [
        OrderResponse(
            order_id_auto_generated=order.order_id_auto_generated,
            order_id=order.order_id,
        )
        for order in orders
    ]
