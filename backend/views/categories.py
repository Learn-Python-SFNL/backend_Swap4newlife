from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend import schemas
from backend.storages.categories import CtStorage

view = Blueprint('categories', __name__)


ctstorage = CtStorage()


@view.get('/')
def categories():
    args = request.args
    title = args.get('title')
    if title:
        category = ctstorage.get_by_title(title)
        new_category = [
            schemas.Category.from_orm(category).dict() for category in category
        ]
        return jsonify(new_category)

    category = ctstorage.get_all()
    all_categories = [
        schemas.Category.from_orm(category).dict()
        for category in category
    ]
    return jsonify(all_categories)


@view.get('/<int:uid>/products/')
def get_products(uid):
    products = ctstorage.get_products_by_category(uid)
    products_in_category = [
        schemas.Product.from_orm(product).dict()
        for product in products
    ]
    return jsonify(products_in_category)


@view.get('/<string:uid>')
def get_categories_by_id(uid):
    category = ctstorage.get_by_id(uid)

    return jsonify(schemas.Category.from_orm(category).dict()), 200


@view.post('/')
def add_categories():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    payload['id'] = -1
    new_category = schemas.Category(**payload)

    category = ctstorage.add(new_category.title)
    return jsonify(schemas.Category.from_orm(category).dict()), 200


@view.put('/<string:uid>')
def update_categories(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    new_category = schemas.Category(**payload)
    category = ctstorage.update(uid, title=new_category.title)
    return jsonify(schemas.Category.from_orm(category).dict()), 200


@view.delete('/<string:uid>')
def delete_category(uid):
    if not ctstorage.delete(uid):
        abort(HTTPStatus.NOT_FOUND)

    return {}, 204
