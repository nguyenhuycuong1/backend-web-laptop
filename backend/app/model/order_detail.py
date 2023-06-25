from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class OrderDetail(SQLModel, table=True):
    __tablename__ = "order_detail"

    order_id: Optional[str] = Field(None, foreign_key="order.order_id", primary_key=True)
    cart_id: Optional[str] = Field(None, foreign_key="cart.cart_id", primary_key=True)
    
    product_id: Optional[str] = Field(None, foreign_key="product.product_id")
