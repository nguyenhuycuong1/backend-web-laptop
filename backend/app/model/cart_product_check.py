from sqlalchemy import Column, String, ForeignKey, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship
import uuid

class CartProductCheck(SQLModel, table=True):
    __tablename__ = "cart_product_check"

    cart_product_check_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True
    )
    product_id: str = Field(
        sa_column=Column("product_id", String, ForeignKey("product.product_id"))
    )
    cart_id: str = Field(
        sa_column=Column("cart_id", String, ForeignKey("cart.cart_id"))
    )

    quantity: int = Field(sa_column=Column("quantity", Integer))
    
    product: "Product" = Relationship(back_populates="cart_product_check")
    cart: "Cart" = Relationship(back_populates="cart_product_check")
    order: "Order" = Relationship(back_populates="cart_product_check")