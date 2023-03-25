from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    products: str

    class Config:
        orm_mode = True
