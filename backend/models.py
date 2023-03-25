from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.db import Base, engine


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    products = relationship('Product', back_populates='category')

    def __repr__(self):
        return f'Category {self.id} {self.title}'


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    category_id = Column(
        Integer,
        ForeignKey('categories.id', onupdate='RESTRICT', ondelete='RESTRICT'),
        nullable=False,
    )
    category = relationship('Category', back_populates='products')

    def __repr__(self):
        return f'Products {self.id} {self.title} {self.category_id}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
