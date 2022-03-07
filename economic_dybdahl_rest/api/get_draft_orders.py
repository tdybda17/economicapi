import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetDraftOrdersAPI(EconomicApi):
    path = 'orders/drafts'

    def __init__(self):
        super().__init__(self.path)

    def get(self, url=None):
        response = requests.get(
            url=self.ECONOMIC_URL if not url else url,
            headers=self.headers
        )
        return response


class GetDraftOrdersInAPI(EconomicApi):
    path = 'orders/drafts?filter=orderNumber$in:'

    def __init__(self):
        super().__init__(self.path)

    def get(self, order_numbers: list, url=None):
        _in = ",".join(order_numbers)
        self.ECONOMIC_URL += '[' + _in + ']'
        response = requests.get(
            url=self.ECONOMIC_URL if not url else url,
            headers=self.headers
        )
        return response
