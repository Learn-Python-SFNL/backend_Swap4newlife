from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend.storages.products import PgStorage

view = Blueprint('products', __name__)


pgstorage = PgStorage()


@view.get('/')
def get_all_products():
    products = pgstorage.get_all()
    all_products = [
        {
            'title': product.title,
            'id': product.id,
            'products': product.products,
        }
        for product in products
    ]

    return jsonify(all_products)


@view.get('/<string:uid>')
def get_product_by_id(uid):
    product = pgstorage.get_by_id(uid)
    if not product:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(
        {
            'title': product.title,
            'products': product.products,
            'id': product.id,
        }), 200


@view.post('/')
def add_product():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    product = pgstorage.add(payload['title'], payload['products'])
    return jsonify(
        {
            'title': product.title,
            'products': product.products,
            'id': product.id,
        }), 200


@view.put('/<string:uid>')
def update_product(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    product = pgstorage.update(payload, uid)
    if not product:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(
        {
            'title': product.title,
            'products': product.products,
            'id': product.id,
        }), 200


@view.delete('/<string:uid>')
def delete_product(uid):
    if not pgstorage.delete(uid):
        abort(HTTPStatus.NOT_FOUND)

    return {}, 204
