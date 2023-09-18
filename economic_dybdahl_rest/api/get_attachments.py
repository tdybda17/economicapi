import requests

from economic_dybdahl_rest.api._api import EconomicApi
from django.conf import settings


class Attachment(EconomicApi):

    path = 'journals/'
    headers = {
        'Content-Type': 'application/pdf',
        'X-AppSecretToken': settings.X_APP_SECRET_TOKEN,
        'X-AgreementGrantToken': settings.X_AGREEMENT_GRANT_TOKEN
    }

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, journal_id, accountingYear, voucherNumber):
        response = requests.get(
            url=self.ECONOMIC_URL + f'{journal_id}/vouchers/{accountingYear}-{voucherNumber}/attachment/file',
            headers=self.headers,
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
