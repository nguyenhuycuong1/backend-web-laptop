from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class InvoiceBase(BaseModel):
    invoice_id: Optional[str] = None

class InvoiceResponse(InvoiceBase):
    order_status: str
    payment_method: str
    total_amount: float
    address: str
    order_id: str
    user_id: str
    
class InvoiceRequest(BaseModel):
    order_status: str
    payment_method: str
    address: str
    total_amount: float
    order_id: str
<<<<<<< HEAD
=======
    user_id: str
>>>>>>> b9aba9b9eb98941130d737ba5cb4df29516c61d0

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


