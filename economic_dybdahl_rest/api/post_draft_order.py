import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.order import Order


class PostDraftOrder(EconomicApi):

    path = 'orders/drafts'

    def __init__(self) -> None:
        super().__init__(self.path)

    def post(self, order: Order):
        response = requests.post(
            url=self.url,
            data=order.to_json(),
            headers=self.headers
        )
        return response
