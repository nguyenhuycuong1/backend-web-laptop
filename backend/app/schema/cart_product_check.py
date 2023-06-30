from pydantic import BaseModel
from typing import Optional


class CartProductCheckBase(BaseModel):
    cart_product_check_id: Optional[str] = None


class CartProductCheckRequest(BaseModel):
    product_id: str
    cart_id: str
    quantity: int


class CartProductCheckResponse(CartProductCheckBase):
    product_id: str
    cart_id: str
    quantity: int

class CartProductCheckItemResponse(BaseModel):
    product_id: str
    cart_id: str
    quantity: int
    