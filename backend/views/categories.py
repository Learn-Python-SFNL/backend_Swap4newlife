from http import HTTPStatus
from uuid import uuid4

from flask import Blueprint, abort, jsonify, request

from backend.storages.categories import CategoryStorage

view = Blueprint('categories', __name__)


init_categories = [
    {
        'id': uuid4().hex,
        'title': 'Книги',
    },
    {
        'id': uuid4().hex,
        'title': 'Растения',
    },
    {
        'id': uuid4().hex,
        'title': 'Товары для дома',
    },
    {
        'id': uuid4().hex,
        'title': 'Музыкальные инструменты',
    },
    {
        'id': uuid4().hex,
        'title': 'Товары для хобби',
    },
    {
        'id': uuid4().hex,
        'title': 'Коллекционирование',
    },
    {
        'id': uuid4().hex,
        'title': 'Мягкие игрушки',
    },
    {
        'id': uuid4().hex,
        'title': 'Женская одежда',
    },
    {
        'id': uuid4().hex,
        'title': 'Мужская одежда',
    },
    {
        'id': uuid4().hex,
        'title': 'Детская одежда',
    },
]


storage = CategoryStorage(init_categories)


@view.get('/')
def get_all_categories():
    return jsonify(storage.get_all())


@view.get('/<string:uid>')
def get_categories_by_id(uid):
    category = storage.get_by_id(uid)
    if not category:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(category), 200


@view.post('/')
def add_categories():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    category = storage.add(payload)

    return jsonify(category), 200


@view.put('/<string:uid>')
def update_categories(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    category = storage.update(uid, payload)
    if not category:
        abort(HTTPStatus.NOT_FOUND)


    return jsonify(category), 200


@view.delete('/<string:uid>')
def delete_category(uid):
    if not storage.delete(uid):
        abort(HTTPStatus.NOT_FOUND)

    return {}, 204
