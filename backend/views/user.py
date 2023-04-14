from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend import schemas
from backend.storages.user import UserStorage

view = Blueprint('users', __name__)

pgstorage = UserStorage()


@view.post('/')
def add_user():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    payload['id'] = -1
    new_user = schemas.User(**payload)

    user = pgstorage.add(new_user.tgid, new_user.username)

    return jsonify(schemas.User.from_orm(user).dict())


@view.get('/telegram/<int:uid>')
def get_by_tgid(uid):
    user = pgstorage.get_by_tgid(tgid=uid)
    return jsonify(schemas.User.from_orm(user).dict())


@view.get('/<int:uid>/products/')
def get_by_product(uid):
    products = pgstorage.get_product_by_user(uid=uid)
    products_in_user = [
        schemas.Product.from_orm(product).dict()
        for product in products
    ]
    return jsonify(products_in_user)
