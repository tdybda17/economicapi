class Response:

    def __init__(self, status_code, data) -> None:
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        if not isinstance(self.data, dict):
            return TypeError('Data should be of type dict')
        return {
            'data': self.data,
            'status_code': self.status_code
        }
