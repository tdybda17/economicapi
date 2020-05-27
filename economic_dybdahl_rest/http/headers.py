class Headers:

    def __init__(self, headers) -> None:
        self.headers = headers
        super().__init__()

    @staticmethod
    def from_request(request):
        return Headers(headers={
            'Content-Type': 'application/json',
            'X-AppSecretToken': request.headers.get('X-AppSecretToken', ''),
            'X-AgreementGrantToken': request.headers.get('X-AgreementGrantToken', ''),
        })
