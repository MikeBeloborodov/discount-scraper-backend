from pydantic import BaseModel, EmailStr


class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
