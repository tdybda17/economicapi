import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetProduct(EconomicApi):

    path = 'products'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, product_number):
        response = requests.get(
            url=self.ECONOMIC_URL + '/' + product_number,
            headers=self.headers
        )
        return response
