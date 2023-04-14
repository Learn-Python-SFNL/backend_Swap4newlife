import logging

from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError
from backend.models import Product, User

logger = logging.getLogger(__name__)


class UserStorage:

    def add(self, tgid: int, username: str) -> User:
        user = User(tgid=tgid, username=username)
        db_session.add(user)
        try:
            db_session.commit()
        except IntegrityError:
            logging.exception('Can not add user')
            raise ConflictError(entity='users', method='add')
        return user

    def get_by_tgid(self, tgid) -> User:
        return User.query.filter(User.tgid == tgid).first()

    def get_product_by_user(self, uid: int) -> Product:
        return Product.query.filter(Product.user_id == uid).all()
