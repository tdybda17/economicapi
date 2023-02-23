import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.product import Product


class PostVouchers(EconomicApi):

    path = 'journals/'

    def __init__(self) -> None:
        super().__init__(self.path)

    def post(self, journal_id, data):
        response = requests.post(
            url=self.ECONOMIC_URL + f'{journal_id}/vouchers',
            json=data,
            headers=self.headers
        )
        return response
