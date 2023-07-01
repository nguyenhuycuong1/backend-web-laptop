from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class OrderBase(BaseModel):
    order_id: Optional[str] = None

class OrderResponse(OrderBase):
    order_id_auto_generated: str
    order_id: str
    
class OrderRequest(BaseModel):
    # order_date: datetime = datetime.now().replace(tzinfo=None)
    product_id: str
    quantity: int
    cart_id: str

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


