from http import HTTPStatus
from uuid import uuid4

from flask import Blueprint, abort, jsonify, request

view = Blueprint('categories', __name__)

storage = [
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


@view.get('/')
def get_all_categories():
    return jsonify(storage)


@view.get('/<string:uid>')
def get_categories_by_id(uid):
    categories = list(filter(lambda category: category['id'] == uid, storage))
    if not categories:
        abort(HTTPStatus.NOT_FOUND)
    return jsonify(categories[0])


@view.post('/')
def add_categories():
    category = {
        'id': uuid4().hex,
        'title': request.json['title'],
    }
    storage.append(category)
    return jsonify(category), 200


@view.put('/<string:uid>')
def update_categories(uid):
    for category in storage:
        if category['id'] == uid:
            category['title'] = request.json.get('title', category['title'])

            return category, 200
    abort(HTTPStatus.NOT_FOUND)


@view.delete('/<string:uid>')
def delete_category(uid):
    for category in storage:
        if category['id'] == uid:
            storage.remove(category)
    return {}, 204
