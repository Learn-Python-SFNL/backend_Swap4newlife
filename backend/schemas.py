from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    category_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    tgid: int
    username: str

    class Config:
        orm_mode = True
