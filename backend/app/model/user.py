from typing import List, Optional
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

from app.model.mixins import TimeMixin
from app.model.user_role import UsersRole

class User(SQLModel,TimeMixin,table=True):
    __tablename__= "user"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    username: str = Field(sa_column=Column("username", String, unique=True))
    email: str = Field(sa_column=Column("email", String, unique=True))
    password: str

    person_id: Optional[str] = Field(default=None, foreign_key="person.id")
    person: Optional["Person"] = Relationship(back_populates="user")

    cart: Optional["Cart"] = Relationship(back_populates="user")
    
    order: List["Order"] = Relationship(back_populates="user")
    
    role: List["Role"] = Relationship(back_populates="user", link_model=UsersRole)