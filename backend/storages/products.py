import logging

from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotfoundError
from backend.models import Product

logger = logging.getLogger(__name__)


class PgStorage:

    def add(self, title: str, category_id: int) -> Product:
        add_product = Product(title=title, category_id=category_id)
        db_session.add(add_product)
        try:
            db_session.commit()
        except IntegrityError:
            logger.exception('Can not add product')
            raise ConflictError(entity='products', method='add')
        return add_product

    def get_all(self) -> list[Product]:
        return Product.query.all()

    def get_by_id(self, uid: int) -> Product:
        products_uid = Product.query.get(uid)
        if not products_uid:
            raise NotfoundError(entity='pruducts', method='get_by_id')
        return products_uid

    def update(self, uid: int, title: str, category_id: int) -> Product:
        product_update = Product.query.get(uid)
        if not product_update:
            raise NotfoundError(entity='products', method='update')
        product_update.title = title
        product_update.category_id = category_id
        try:
            db_session.commit()
        except IntegrityError:
            logger.exception('Can not update product')
            raise ConflictError(entity='products', method='update')
        return product_update

    # TODO: добавить  not_foudn.error, conflict.error
    def delete(self, uid: int):
        delete_product = Product.query.get(uid)
        if not delete_product:
            raise NotfoundError(entity='products', method='delete')
        db_session.delete(delete_product)
        try:
            db_session.commit()
        except IntegrityError:
            logger.exception('Can not delete product')
            raise ConflictError(entity='products', method='delete')
