import zeep
from django.http import JsonResponse
from zeep import Settings
from requests import Session

from economicapi import settings
from economicapi.settings import X_APP_SECRET_TOKEN, X_AGREEMENT_GRANT_TOKEN
from zeep.transports import Transport


class EconomicSOAPApi:
    wsdl = 'https://api.e-conomic.com/secure/api1/EconomicWebService.asmx?wsdl'
    settings = Settings()
    session = Session()
    transport = Transport(session=session)
    client = zeep.Client(wsdl=wsdl, settings=settings, transport=transport)

    def __init__(self) -> None:
        self.login()
        super().__init__()

    def login(self):
        self.client.service.ConnectWithToken(
            token=X_AGREEMENT_GRANT_TOKEN,
            appToken=X_APP_SECRET_TOKEN
        )
