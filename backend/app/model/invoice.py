from typing import List, Optional
from sqlalchemy import Column, String
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import ForeignKey
import uuid


class Invoice(SQLModel, table=True):
    __tablename__ = "invoice"

    invoice_id: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True
    )
    
    order_id_auto_generated: Optional[str] = Field(default=None, foreign_key="order.order_id_auto_generated")
    order: Optional["Order"] = Relationship(back_populates="invoice")
    
    order_date: datetime = Field(default_factory=datetime.now)
    order_status: str = Field(sa_column=Column("order_status", String))
    payment_method: str = Field(sa_column=Column("payment", String))
    address: str = Field(sa_column=Column("address", String))
