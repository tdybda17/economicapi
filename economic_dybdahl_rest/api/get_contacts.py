from economic_dybdahl_rest.api._api import EconomicApi
import requests


class GetContactsApi(EconomicApi):
    path = 'customers'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self, customer_number, skip_pages=0, page_size=20):
        response = requests.get(
            url=f'{self.ECONOMIC_URL}/{customer_number}/contacts?skippages={skip_pages}&pagesize={page_size}',
            headers=self.headers
        )
        return response
