import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetProducts(EconomicApi):

    path = 'products?filter=productNumber$in:'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, product_numbers: list):
        _in = ",".join(product_numbers)
        self.ECONOMIC_URL += '[' + _in + ']'
        response = requests.get(
            url=self.ECONOMIC_URL,
            headers=self.headers
        )
        return response
