import requests

from economic_dybdahl_rest.api._api import EconomicApi


class ListPaymentTermsAPI(EconomicApi):
    path = 'payment-terms'

    def __init__(self):
        super().__init__(self.path)


    def get(self, url=None):
        response = requests.get(
            url=self.ECONOMIC_URL if not url else url,
            headers=self.headers
        )
        return response
