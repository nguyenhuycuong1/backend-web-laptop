from typing import List, Optional
from sqlalchemy import Column, String
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

from app.model.order_detail import OrderDetail

class Order(SQLModel, table=True):
    __tablename__ = "order"

    order_id: Optional[str] = Field(None, primary_key=True, nullable=False)
    order_date: datetime = Field(default_factory=datetime.now)
    order_status: str = Field(sa_column=Column("order_status", String))
    payment: str = Field(sa_column=Column("payment", String))

    user_id: Optional[str] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="order")
    
    cart: List["Cart"] = Relationship(back_populates="order", link_model=OrderDetail)