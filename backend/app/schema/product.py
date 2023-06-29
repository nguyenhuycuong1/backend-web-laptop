from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    product_id: str


class ProductCreateRequest(ProductBase):
    product_name: str
    description: str
    price: float
    image: str


class ProductUpdateRequest(ProductBase):
    pass


class ProductItemResponse(ProductBase):
    product_name: str
    description: str
    price: float
    image: str


class ProductListResponse(BaseModel):
    product_id: str
    product_name: str
    description: str
    price: float
    image: str
    brand_id: str
