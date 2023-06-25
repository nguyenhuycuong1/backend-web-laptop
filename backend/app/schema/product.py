from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    product_id: str
    order_status: str

class ProductCreateRequest(ProductBase):
    product_name: str
    description: str
    price: str
    image: str

class ProductUpdateRequest(ProductBase):
    pass

class ProductItemResponse(ProductBase):
    order_date: datetime

class ProductListResponse(BaseModel):
    product_id: str
    product_name: str
    description: str
    price: str
    image: str