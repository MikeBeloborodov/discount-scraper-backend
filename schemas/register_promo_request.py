from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum


class CathegoryEnum(str, Enum):
    sushi = 'sushi'
    pizza = 'pizza'
    kebab = 'kebab'
    fast_food = 'fast_food'


class RegisterPromoRequest(BaseModel):
    title: str
    old_price: Optional[str]
    new_price: str
    cathegory: CathegoryEnum
    weight: Optional[str]
    img: Optional[HttpUrl]
    website: HttpUrl
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True
        