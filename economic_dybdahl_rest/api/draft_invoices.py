import json

import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.order import Order


class PostInvoicesDraft(EconomicApi):

    path = 'invoices/drafts'

    def __init__(self) -> None:
        super().__init__(self.path)

    def post(self, invoice):
        response = requests.post(
            url=self.ECONOMIC_URL,
            data=json.dumps(invoice),
            headers=self.headers
        )
        return response
