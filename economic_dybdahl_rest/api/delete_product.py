import requests

from economic_dybdahl_rest.api._api import EconomicApi


class DeleteProductApi(EconomicApi):

    path = 'products'

    def __init__(self) -> None:
        super().__init__(self.path)

    def delete(self, product_number):
        response = requests.delete(
            url=self.ECONOMIC_URL + '/' + product_number,
            headers=self.headers
        )
        return response
