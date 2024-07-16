import requests

from economic_dybdahl_rest.api._api import EconomicApi


class JournalVoucherAttachmentAPI(EconomicApi):

    path = 'journals/'
    updated_headers = dict()

    def __init__(self) -> None:
        self.updated_headers = dict(self.headers)
        self.updated_headers['Content-Type'] = None
        super().__init__(self.path)

    def patch(self, journal_number, accounting_year_voucher_number, data):
        response = requests.patch(
            url=self.ECONOMIC_URL + str(journal_number) + '/vouchers/' + str(accounting_year_voucher_number) + '/attachment/file',
            headers=self.updated_headers,
            files=data
        )
        return response
