from pydantic import BaseModel


class CartBase(BaseModel):
    cart_id: str

class CartResponse(CartBase):
    user_id: str
