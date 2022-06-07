from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    access_token_expire_minutes: int
    algorithm: str
    secret_key: str

    class Config:
        env_file = '.env'


settings = Settings()
