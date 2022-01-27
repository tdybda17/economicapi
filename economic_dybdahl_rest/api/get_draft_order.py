import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetDraftOrderAPI(EconomicApi):

    path = 'orders/drafts/'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, order_number):
        response = requests.get(
            url=self.ECONOMIC_URL + str(order_number),
            headers=self.headers
        )
        return response
