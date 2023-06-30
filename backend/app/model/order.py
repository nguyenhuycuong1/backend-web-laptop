from typing import List, Optional
from sqlalchemy import Column, String, Float
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import ForeignKey
import uuid


class Order(SQLModel, table=True):
    __tablename__ = "order"

    order_id: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True
    )
    order_date: datetime = Field(default_factory=datetime.now)
    order_status: str = Field(sa_column=Column("order_status", String))
    payment_method: str = Field(sa_column=Column("payment", String))
    address: str = Field(sa_column=Column("address", String))
    total_amount: float = Field(sa_column=Column("total_amount", Float))

    cart_product_check_id: str = Field(
        sa_column=Column(
            "cart_product_check_id",
            String,
            ForeignKey("cart_product_check.cart_product_check_id"),
            unique=True,
        )
    )
    user_id: str = Field(
        sa_column=Column(
            "user_id",
            String,
            ForeignKey("user.id"),
            unique=True,
        )
    )
    cart_product_check: "CartProductCheck" = Relationship(back_populates="order")
    user: Optional["User"] = Relationship(back_populates="order")
