from http import HTTPStatus
from uuid import uuid4

from flask import Blueprint, abort, jsonify, request

from backend.storages.products import ProductStorage

view = Blueprint('products', __name__)


init_products = [
    {
        'title': 'Книга по Python',
        'products': 'Книга',
        'id': uuid4().hex,
    },

    {
        'title': 'Книга по JS',
        'products': 'Книга',
        'id': uuid4().hex,
    },
]


storage = ProductStorage(init_products)


@view.get('/')
def get_all_products():
    return jsonify(storage.get_all())


@view.get('/<string:uid>')
def get_product_by_id(uid):
    product = storage.get_by_id(uid)
    if not product:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(product), 200


@view.post('/')
def add_product():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    product = storage.add(payload)

    return jsonify(product), 200


@view.put('/<string:uid>')
def update_product(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    product = storage.update(uid, payload)
    if not product:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(product), 200


@view.delete('/<string:uid>')
def delete_product(uid):
    if not storage.delete(uid):
        abort(HTTPStatus.NOT_FOUND)

    return {}, 204
