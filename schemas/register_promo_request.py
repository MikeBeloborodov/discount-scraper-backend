from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum


class CategoryEnum(str, Enum):
    sushi = 'sushi'
    pizza = 'pizza'
    kebab = 'kebab'
    shawarma = 'shawarma'
    dumplings = 'dumplings'
    pie = 'pie'
    burger = 'burger'
    combo = 'combo'


class RegisterPromoRequest(BaseModel):
    title: str
    old_price: Optional[int]
    new_price: int
    category: CategoryEnum
    weight: Optional[str]
    ingredients: Optional[str]
    img: Optional[HttpUrl]
    website_link: HttpUrl
    website_title: str
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True
        