from pydantic import BaseModel
from typing import Optional


class CartProductCheckBase(BaseModel):
    cart_product_check_id: Optional[str] = None


class CartProductRequest(BaseModel):
    product_id: str
    cart_id: str
    quantity: int


class CartProductResponse(CartProductCheckBase):
    product_id: str
    cart_id: str
    quantity: int

    