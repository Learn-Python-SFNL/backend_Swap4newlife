from sqlalchemy import Column, Integer, String

from backend.db import Base, engine


class User(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self):
        return f'Category {self.id} {self.title}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
