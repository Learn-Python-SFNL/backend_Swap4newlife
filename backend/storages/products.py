from uuid import uuid4


class ProductStorage:

    def __init__(self, products) -> None:
        self.storage = {product['id']: product for product in products}

    def get_all(self):
        return list(self.storage.values())

    def get_by_id(self, uid: str):
        self.product = self.storage.get(uid)
        return self.product

    def add(self, product):
        product['id'] = uuid4().hex
        self.storage[product['id']] = product
        return product

    def update(self, uid: str, new_product):
        old_product = self.storage.get(uid)
        if not old_product:
            return None

        old_product.update(new_product)
        return old_product

    def delete(self, uid: str) -> bool:
        if uid not in self.storage:
            return False

        self.storage.pop(uid)
        return True
