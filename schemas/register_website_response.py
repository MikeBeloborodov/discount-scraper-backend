from enum import Enum
from pydantic import BaseModel, HttpUrl


class CathegoryEnum(str, Enum):
    sushi = 'sushi'
    pizza = 'pizza'
    kebab = 'kebab'
    fast_food = 'fast_food'
    shawarma = 'shawarma'
    dumplings = 'dumplings'
    pie = 'pie'
    burger = 'burger'


class RegisterWebsiteResponse(BaseModel):
    item_id: int
    title: str
    link: HttpUrl
    phone_number: str
    cathegory: CathegoryEnum

    class Config:
        orm_mode = True
        