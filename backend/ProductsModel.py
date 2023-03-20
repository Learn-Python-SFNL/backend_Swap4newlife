from sqlalchemy import Column, Integer, String

from backend.db import Base, engine


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    products = Column(String)

    def __repr__(self):
        return f'Products {self.id} {self.title} {self.products}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
