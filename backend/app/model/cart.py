from typing import List, Optional
from sqlalchemy import Column, String
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

from app.model.mixins import TimeMixin
from app.model.order_detail import OrderDetail
from app.model.cart_product import CartProduct


class Cart(SQLModel, TimeMixin, table=True):
    __tablename__ = "cart"

    cart_id: Optional[str] = Field(None, primary_key=True, nullable=False)
    cart_date: datetime = Field(default_factory=datetime.now)
    cart_status: str = Field(sa_column=Column("cart_status", String))

    user_id: Optional[str] = Field(default=None, foreign_key="user.id", unique=True)
    user: Optional["User"] = Relationship(back_populates="cart")
    
    order: List["Order"] = Relationship(back_populates="cart", link_model=OrderDetail)
    product: List["Product"] = Relationship(
        back_populates="cart", link_model=CartProduct
    )
