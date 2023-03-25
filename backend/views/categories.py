from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend.storages.categories import CtStorage

view = Blueprint('categories', __name__)


ctstorage = CtStorage()


@view.get('/')
def get_all_categories():
    categories = ctstorage.get_all()
    response = [{'id': category.id, 'title': category.title} for category in categories]
    return jsonify(response)


@view.get('/<string:uid>')
def get_categories_by_id(uid):
    category = ctstorage.get_by_id(uid)
    if not category:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify({'title': category.title, 'id': category.id}), 200


@view.post('/')
def add_categories():
    category = request.json
    if not category:
        abort(HTTPStatus.BAD_REQUEST)

    new_category = ctstorage.add(category['title'])

    return jsonify({'title': new_category.title, 'id': new_category.id}), 200


@view.put('/<string:uid>')
def update_categories(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    category = ctstorage.update(payload=payload, uid=uid)
    if not category:
        abort(HTTPStatus.NOT_FOUND)
    return jsonify({'title': category.title, 'id': category.id}), 200


@view.delete('/<string:uid>')
def delete_category(uid):
    if not ctstorage.delete(uid):
        abort(HTTPStatus.NOT_FOUND)

    return {}, 204
