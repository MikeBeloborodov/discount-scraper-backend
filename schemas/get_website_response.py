from pydantic import BaseModel, HttpUrl


class GetWebsiteResponse(BaseModel):
    item_id: int
    title: str
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True
        