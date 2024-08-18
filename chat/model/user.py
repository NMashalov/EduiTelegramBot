from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    telegram_login: str
    name: str
    surname: str

    class Config:
        orm_mode = True
