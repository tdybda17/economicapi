import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.product import Product


class PutProduct(EconomicApi):

    path = 'products'

    def __init__(self) -> None:
        super().__init__(self.path)

    def put(self, product: Product):
        self.url += '/' + product.product_number
        response = requests.put(
            url=self.url,
            data=product.to_json(),
            headers=self.headers
        )
        return response
