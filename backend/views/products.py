from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend import schemas
from backend.storages.products import PgStorage

view = Blueprint('products', __name__)


pgstorage = PgStorage()


@view.get('/')
def get_all_products():
    products = pgstorage.get_all()
    all_products = [
        schemas.Product.from_orm(product).dict()
        for product in products
    ]

    return jsonify(all_products)


@view.get('/<string:uid>')
def get_product_by_id(uid):
    product = pgstorage.get_by_id(uid)

    return jsonify(schemas.Product.from_orm(product).dict()), 200


@view.post('/')
def add_product():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    payload['id'] = -1
    new_product = schemas.Product(**payload)

    product = pgstorage.add(
        new_product.title,
        new_product.category_id,
        new_product.user_id,
    )

    return jsonify(schemas.Product.from_orm(product).dict()), 200


@view.put('/<string:uid>')
def update_product(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    new_product = schemas.Product(**payload)
    product = pgstorage.update(uid, title=new_product.title, category_id=new_product.category_id)

    return jsonify(schemas.Product.from_orm(product).dict()), 200


@view.delete('/<string:uid>')
def delete_product(uid):
    pgstorage.delete(uid)

    return {}, 204
