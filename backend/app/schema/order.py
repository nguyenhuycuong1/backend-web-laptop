from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class OrderBase(BaseModel):
    user_id: str

class OrderResponse(OrderBase):
    order_id: str
    order_date: datetime
    order_status: str
    payment: str
    
class OrderListResponse(OrderResponse):
    user_id: str
