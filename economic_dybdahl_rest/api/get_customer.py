import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetCustomerApi(EconomicApi):

    path = 'customers'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, customer_number):
        response = requests.get(
            url=self.ECONOMIC_URL + '/' + customer_number,
            headers=self.headers
        )
        return response
