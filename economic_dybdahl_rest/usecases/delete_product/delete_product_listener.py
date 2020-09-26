import json

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class DeleteProductListener(Listener):

    def on_success(self):
        self.response = Response(
            status_code=200,
            data={'message': 'product updated'}
        )

    def on_does_not_exist(self):
        self.response = Response(
            status_code=404,
            data={'message': 'Product not found'}
        )

    def on_product_in_use(self):
        self.response = Response(
            status_code=400,
            data={'message': 'Product is in use'}
        )

    def on_unknown_error(self, status_code, content):
        content_dict = json.loads(content.decode("utf-8"))
        content_dict['status_code'] = status_code
        self.response = Response(
            status_code=520,
            data=content_dict
        )

    def on_not_authorized(self):
        self.response = Response(
            status_code=401,
            data={'message': 'not authorized'}
        )
