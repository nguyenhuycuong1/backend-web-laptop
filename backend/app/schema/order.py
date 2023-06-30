from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class OrderBase(BaseModel):
    order_id: Optional[str] = None

class OrderResponse(OrderBase):
    order_date: datetime
    order_status: str
    payment_method: str
    address: str
    total_amount: float
    cart_product_check_id: str
    user_id: str
    
class OrderRequest(BaseModel):
    order_date: datetime = datetime.now().replace(tzinfo=None)
    order_status: str
    payment_method: str
    address: str
    total_amount: float
    cart_product_check_id: str
    user_id: str

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


