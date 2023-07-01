from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class OrderBase(BaseModel):
    order_id: Optional[str] = None

class OrderResponse(OrderBase):
    product_id: str
    quantity: int
    cart_id: str
    total_amount: float
    
class OrderRequest(BaseModel):
    # order_date: datetime = datetime.now().replace(tzinfo=None)
    product_id: str
    quantity: int
    cart_id: str
    total_amount: float

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


