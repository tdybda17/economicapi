class EconomicApi:

    url = 'https://restapi.e-conomic.com/'
    headers = {
        'Content-Type': 'application/json',
        'X-AppSecretToken': 'demo',
        'X-AgreementGrantToken': 'demo'
    }

    def __init__(self, path) -> None:
        self.url += path
