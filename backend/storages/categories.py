from typing import Any

from backend.db import db_session
from backend.models import Category


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

    def update(self, payload: dict[str, Any], uid: int) -> Category:
        category_update = Category.query.get(uid)
        category_update.title = payload['title']
        db_session.commit()
        return category_update

    def delete(self, uid: int) -> bool:
        category_delete = Category.query.get(uid)
        if not category_delete:
            return False
        db_session.delete(category_delete)
        db_session.commit()
        return True
