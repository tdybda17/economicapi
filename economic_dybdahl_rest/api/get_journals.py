import requests

from economic_dybdahl_rest.api._api import EconomicApi


class GetJournalsAPI(EconomicApi):

    path = 'journals'

    def __init__(self) -> None:
        super().__init__(self.path)

    def get(self):
        response = requests.get(
            url=self.ECONOMIC_URL,
            headers=self.headers
        )
        return response

    def get_next_page(self, next_page_url):
        response = requests.get(
            url=next_page_url,
            headers=self.headers
        )
        return response