from typing import Any

from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError
from backend.models import Product


class PgStorage:

    def add(self, title: str, products: str) -> Product:
        add_product = Product(title=title, products=products)
        db_session.add(add_product)
        try:
            db_session.commit()
        except IntegrityError:
            raise ConflictError(entity='products', method='add')
        return add_product

    def get_all(self) -> list[Product]:
        return Product.query.all()

    # TODO: добавить  not_foudn.error
    def get_by_id(self, uid: int) -> Product:
        return Product.query.get(uid)

    # TODO: добавить conflict.erro, not_foudn.error
    def update(self, uid: int, title: str, products: str) -> Product:
        product_update = Product.query.get(uid)
        product_update.title = title
        product_update.products = products
        db_session.commit()
        return product_update

    # TODO: добавить  not_foudn.error
    def delete(self, uid: int) -> bool:
        delete_product = Product.query.get(uid)
        if not delete_product:
            return False

        db_session.delete(delete_product)
        db_session.commit()
        return True
