import requests

from economic_dybdahl_rest.api._api import EconomicApi
from economic_dybdahl_rest.dto.product import Product


class Attachment(EconomicApi):

    path = 'journals/'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, journal_id, accountingYear, voucherNumber):
        pdfHeaders = self.headers
        pdfHeaders['Content-Type'] = 'application/pdf'
        response = requests.get(
            url=self.ECONOMIC_URL + f'{journal_id}/vouchers/{accountingYear}-{voucherNumber}/attachment/file',
            headers=pdfHeaders,
        )
        return response


class HasAttachment(EconomicApi):
    path = 'journals/'
    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, journal_id, accountingYear, voucherNumber):
        response = requests.get(
            url=self.ECONOMIC_URL + f'{journal_id}/vouchers/{accountingYear}-{voucherNumber}/attachment/',
            headers=self.headers
        )
        return response
