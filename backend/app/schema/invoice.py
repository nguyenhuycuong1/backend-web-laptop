from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class InvoiceBase(BaseModel):
    invoice_id: Optional[str] = None

class InvoiceResponse(InvoiceBase):
    order_date: datetime
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
    user_id: str

<<<<<<< HEAD

=======
class InvoiceAddressRequest(BaseModel):
    address: str
    
>>>>>>> bf7f40c9380f7964e74c8f4314b5746e51433c9e
class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


