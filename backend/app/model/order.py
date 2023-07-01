from typing import Optional
from sqlalchemy import Column, String, Float, Integer
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlmodel import ForeignKey
import uuid
import sqlalchemy as sa

from app.model.invoice import Invoice

from app.model.invoice import Invoice

class Order(SQLModel, table=True):
    __tablename__ = "order"

    order_id_auto_generated: str = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True
    )
    order_id: str = Field(sa_column=Column("order_id", String))
    
    invoice: Optional[Invoice] = Relationship(back_populates="order")
    
    product_id: str = Field(sa_column=Column("product_id", String, unique=True))
    quantity: int = Field(sa_column=Column("quantity", Integer))
    total_amount: float = Field(sa_column=Column("total_amount", Float))
    
    cart_id: Optional[str] = Field(default=None, foreign_key="cart.cart_id")
    cart: Optional["Cart"] = Relationship(back_populates="order")