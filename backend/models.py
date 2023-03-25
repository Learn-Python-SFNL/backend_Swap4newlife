from sqlalchemy import Column, Integer, String

from backend.db import Base, engine


class Categories(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self):
        return f'Category {self.id} {self.title}'


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    products = Column(String)

    def __repr__(self):
        return f'Products {self.id} {self.title} {self.products}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
