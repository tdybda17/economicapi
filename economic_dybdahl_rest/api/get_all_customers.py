import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetAllCustomersApi(EconomicApi):

    path = 'customers'

    def __init__(self) -> None:
        super().__init__(self.path)


    def get(self, url=None):
        response = requests.get(
            url=self.ECONOMIC_URL + '/' if not url else url,
            headers=self.headers
        )
        return response
