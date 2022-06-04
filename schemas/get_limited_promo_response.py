from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime
from enum import Enum


class CathegoryEnum(str, Enum):
    sushi = 'sushi'
    pizza = 'pizza'
    kebab = 'kebab'
    fast_food = 'fast_food'


class GetLimitedPromoResponse(BaseModel):
    item_id: int
    created_at: datetime
    updated_at: datetime
    title: str
    old_price: Optional[int]
    new_price: int
    cathegory: CathegoryEnum
    weight: Optional[str]
    img: Optional[HttpUrl]
    website_link: HttpUrl
    website_title: str
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True