from pydantic import BaseModel


class LoginUserResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
