import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetBookedInvoiceAPI(EconomicApi):

    path = 'invoices/booked/'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, booked_number):
        response = requests.get(
            url=self.ECONOMIC_URL + str(booked_number),
            headers=self.headers
        )
        return response
