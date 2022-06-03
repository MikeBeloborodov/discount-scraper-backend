from pydantic import BaseModel, HttpUrl


class RegisterWebsiteResponse(BaseModel):
    item_id: int
    title: str
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True
        