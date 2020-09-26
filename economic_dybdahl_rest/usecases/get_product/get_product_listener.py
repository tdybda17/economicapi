import json

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetProductListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data=json.loads(data.decode("utf-8"))
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            status_code=status_code,
            data=json.load(content.decode('utf-8'))
        )

    def on_does_on_exist(self):
        self.response = Response(
            status_code=404,
            data={'message': 'Product does not exist'}
        )
