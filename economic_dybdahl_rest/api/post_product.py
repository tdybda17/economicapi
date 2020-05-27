import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.product import Product


class PostProduct(EconomicApi):

    path = 'products'

    def __init__(self) -> None:
        super().__init__(self.path)

    def post(self, product: Product):
        response = requests.post(
            url=self.url,
            data=product.to_json(),
            headers=self.headers
        )
        return response
