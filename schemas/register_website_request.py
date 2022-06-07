from enum import Enum
from pydantic import BaseModel, HttpUrl


class CategoryEnum(str, Enum):
    sushi = 'sushi'
    pizza = 'pizza'
    kebab = 'kebab'
    shawarma = 'shawarma'
    dumplings = 'dumplings'
    pie = 'pie'
    burger = 'burger'
    combo = 'combo'


class RegisterWebsiteRequest(BaseModel):
    title: str
    link: HttpUrl
    phone_number: str
    category: CategoryEnum

    class Config:
        orm_mode = True
        