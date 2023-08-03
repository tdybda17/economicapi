import json
from dataclasses import dataclass

import requests

from economic_dybdahl_rest.api._api import EconomicApi


@dataclass
class BookDraftInvoiceRequest:
    draft_invoice_number: int
    book_with_number: int = None
    send_by_ean: bool = False

    def get_post_body(self):
        body = dict(
            draftInvoice=dict(draftInvoiceNumber=int(self.draft_invoice_number)),
        )

        if self.book_with_number:
            body['bookWithNumber'] = int(self.book_with_number)

        if self.send_by_ean:
            body['sendBy'] = 'ean'

        return json.dumps(body)


class BookDraftInvoiceAPI(EconomicApi):
    path = 'invoices/booked'

    def __init__(self):
        super().__init__(self.path)

    def post(self, body: BookDraftInvoiceRequest):
        response = requests.post(
            url=self.ECONOMIC_URL,
            headers=self.headers,
            data=body.get_post_body()
        )
        return response
