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
    address: str
    order_id: str
    order_id_auto_generated: str
    
class InvoiceRequest(BaseModel):
    order_date: datetime
    order_status: str
    payment_method: str
    address: str
    total_amount: str
    order_id: str
    order_id_auto_generated: str

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


