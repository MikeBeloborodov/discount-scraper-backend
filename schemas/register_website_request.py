from pydantic import BaseModel, HttpUrl


class RegisterWebsiteRequest(BaseModel):
    title: str
    link: HttpUrl
    phone_number: str

    class Config:
        orm_mode = True
        