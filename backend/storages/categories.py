import logging

# from sqlalchemy.exc import IntegrityError

from backend.db import db_session
# from backend.errors import ConflictError, NotfoundError
from backend.models import Category

logger = logging.getLogger(__name__)


class CtStorage:

    def add(self, title: str) -> Category:
        add_project = Category(title=title)
        db_session.add(add_project)
        db_session.commit()
        return add_project

    def get_all(self) -> list[Category]:
        return Category.query.all()

    def get_by_id(self, uid) -> Category:
        return Category.query.get(uid)

    def update(self, uid: int, title: str) -> Category:
        category = Category.query.get(uid)
        category.title = title
        db_session.commit()
        return category

    def delete(self, uid: int) -> bool:
        category_delete = Category.query.get(uid)
        if not category_delete:
            return False
        db_session.delete(category_delete)
        db_session.commit()
        return True
