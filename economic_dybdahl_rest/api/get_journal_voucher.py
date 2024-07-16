import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetJournalVoucherAPI(EconomicApi):

    path = 'journals/'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, journal_number, accounting_year_voucher_number):
        response = requests.get(
            url=self.ECONOMIC_URL + str(journal_number) + '/vouchers/' + str(accounting_year_voucher_number),
            headers=self.headers
        )
        return response