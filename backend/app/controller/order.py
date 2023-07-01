from fastapi import APIRouter, HTTPException
from app.model.order import Order
from sqlalchemy.future import select
from app.config import db, commit_rollback
from typing import List
from app.schema.order import OrderBase, OrderRequest, OrderResponse, ResponseSchema, OrderItemResponse, OrderSearchParams
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
            order_id=order.order_id
        )
        for order in orders
    ]
    
@router.get("/order/{order_id}", response_model=List[OrderItemResponse])
async def get_order_by_id(order_id: str):
    query = select(Order).where(Order.order_id == order_id)
    result = await db.session.execute(query)
    order = result.scalars().all()

    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")