from flask import Flask, jsonify, request, abort
from http import HTTPStatus
from uuid import uuid4


app = Flask(__name__)

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
    }
]

@app.route('/api/v1/categories/', methods=['GET'])
def get_all_categories():
    return jsonify(storage)


@app.get('/api/v1/categories/<string:uid>')
def get_categories_by_id(uid):
    categories = list(filter(lambda category: category['id'] == uid, storage))
    if len(categories) == 0:
        abort(404)
    return jsonify(categories[0])


@app.post('/api/v1/categories/')
def add_categories():
    category = {
        'id': uuid4().hex,
        'title': request.json['title'],
    }
    storage.append(category)
    return jsonify(category), 200


@app.put('/api/v1/categories/<string:uid>')
def update_categories(uid):
    for category in storage:
        if category["id"] == uid:
            category['title'] = request.json.get('title',category['title'])

    return category, 200


@app.delete('/api/v1/categories/<string:uid>')
def delete_category(uid):
    for category in storage:
        if category["id"] == uid:
            storage.remove(category)
    return {}, 204


if __name__ == '__main__':
    app.run(debug=True)
