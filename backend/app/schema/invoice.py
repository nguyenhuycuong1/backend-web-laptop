from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class InvoiceBase(BaseModel):
    invoice_id: Optional[str] = None

class InvoiceResponse(InvoiceBase):
    order_date: datetime = datetime.now().replace(tzinfo=None)
    order_status: str
    payment_method: str
    total_amount: str
    address: str
    order_id: str
    order_id_auto_generated: str
    
class InvoiceRequest(BaseModel):
    order_date: datetime = datetime.now().replace(tzinfo=None)
    order_status: str
    payment_method: str
    address: str
    total_amount: str
    order_id: str
    order_id_auto_generated: str

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


