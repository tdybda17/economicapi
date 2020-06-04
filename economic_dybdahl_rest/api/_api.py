from economicapi import settings


class EconomicApi:

    ECONOMIC_URL = 'https://restapi.e-conomic.com/'
    headers = {
        'Content-Type': 'application/json',
        'X-AppSecretToken': settings.X_APP_SECRET_TOKEN,
        'X-AgreementGrantToken': settings.X_AGREEMENT_GRANT_TOKEN
    }

    def __init__(self, path) -> None:
        self.ECONOMIC_URL += path
