from http import HTTPStatus
from uuid import uuid4

from flask import Blueprint, abort, jsonify, request

view = Blueprint('categories', __name__)

categories = [
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

storage = {category['id']: category for category in categories}


@view.get('/')
def get_all_categories():
    return jsonify(list(storage.values()))


@view.get('/<string:uid>')
def get_categories_by_id(uid):
    category = storage.get(uid)
    if category:
        return jsonify(category), 200
    abort(HTTPStatus.NOT_FOUND)


@view.post('/')
def add_categories():
    category = request.json
    if not category:
        abort(HTTPStatus.BAD_REQUEST)

    category['id'] = uuid4().hex
    storage[category['title']] = category
    return jsonify(category), 200


@view.put('/<string:uid>')
def update_categories(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    category = storage.get(uid)
    if not category:
        abort(HTTPStatus.NOT_FOUND)

    category.update(payload)
    return jsonify(category), 200


@view.delete('/<string:uid>')
def delete_category(uid):
    if uid not in storage:
        abort(HTTPStatus.NOT_FOUND)

    storage.pop(uid)
    return {}, 204
