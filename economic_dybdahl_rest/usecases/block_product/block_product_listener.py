import json

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class BlockProductListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data={'message': 'Product blocked'}
        )

    def on_unknown_error(self, status_code, content):
        content_dict = json.loads(content.decode("utf-8"))
        content_dict['status_code'] = status_code
        self.response = Response(
            status_code=520,
            data=content_dict
        )

    def on_does_not_exist(self):
        self.response = Response(
            status_code=404,
            data={'message': 'Not found'}
        )

    def on_unable_to_convert_to_int(self):
        self.response = Response(
            status_code=501,
            data={'message': 'E-conomic inventory get error'}
        )

    def on_product_in_stock(self):
        self.response = Response(
            status_code=409,
            data={'message': 'Product is in stock'}
        )
