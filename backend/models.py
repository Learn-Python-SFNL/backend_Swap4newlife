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


class Choose(Base):

    __tablename__ = 'chooses'

    source_product_id = Column(
        Integer,
        ForeignKey('products.id', onupdate='RESTRICT', ondelete='RESTRICT'),
        primary_key=True,
    )
    target_product_id = Column(
        Integer,
        ForeignKey('products.id', onupdate='RESTRICT', ondelete='RESTRICT'),
        primary_key=True,
    )

    source_product = relationship(
        'Product',
        foreign_keys=[source_product_id],
        back_populates='choose_sources',
    )
    target_product = relationship(
        'Product',
        foreign_keys=[target_product_id],
        back_populates='choose_targets',
    )


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

    user_id = Column(
        Integer,
        ForeignKey('users.id', onupdate='RESTRICT', ondelete='RESTRICT'),
        nullable=False,
    )
    user = relationship('User', back_populates='products')

    def __repr__(self):
        return f'Products {self.id} {self.title} {self.category_id}'

    choose_sources = relationship(
        'Choose',
        foreign_keys=Choose.source_product_id,
        back_populates='target_product',
    )
    choose_targets = relationship(
        'Choose',
        foreign_keys=Choose.target_product_id,
        back_populates='source_product',
    )


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tgid = Column(Integer, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    products = relationship('Product', back_populates='user')

    def __repr__(self):
        return f'Users {self.id} {self.tgid} {self.username}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
