class EconomicApi:

    ECONOMIC_URL = 'https://restapi.e-conomic.com/'
    headers = {
        'Content-Type': 'application/json',
        'X-AppSecretToken': '',
        'X-AgreementGrantToken': ''
    }

    def __init__(self, path) -> None:
        self.ECONOMIC_URL += path
