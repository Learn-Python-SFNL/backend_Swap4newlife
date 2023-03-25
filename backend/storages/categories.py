from typing import Any

from backend.db import db_session
from backend.models import Categories


class CtStorage:

    def add(self, title: str) -> Categories:
        add_project = Categories(title=title)
        db_session.add(add_project)
        db_session.commit()
        return add_project

    def get_all(self) -> list[Categories]:
        return Categories.query.all()

    def get_by_id(self, uid) -> Categories:
        return Categories.query.get(uid)

    def update(self, payload: dict[str, Any], uid: int) -> Categories:
        category_update = Categories.query.get(uid)
        category_update.title = payload['title']
        db_session.commit()
        return category_update

    def delete(self, uid: int) -> bool:
        category_delete = Categories.query.get(uid)
        if not category_delete:
            return False
        db_session.delete(category_delete)
        db_session.commit()
        return True
