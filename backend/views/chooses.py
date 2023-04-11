from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from backend import schemas
from backend.storages.chooses import ChoosesStorage

view = Blueprint('chooses', __name__)

chstorage = ChoosesStorage()


@view.post('/')
def chooses():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST)

    choose_products = schemas.Choose(**payload)

    product = chstorage.add(
        choose_products.source_product_id,
        choose_products.target_product_id,
    )

    return jsonify(schemas.Choose.from_orm(product).dict())
