import json

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class SyncProductListener(Listener):

    def on_validation_error(self, error_msg):
        self.response = Response(
            status_code=400,
            data={'message': error_msg}
        )

    # product created
    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data={'message': 'product updated'}
        )

    def on_product_created(self):
        self.response = Response(
            status_code=201,
            data={'message': 'product created'}
        )

    def on_schema_validation_error(self, content):
        self.response = Response(
            status_code=400,
            data=json.loads(content.decode("utf-8"))
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

    def on_forbidden(self, content):
        self.response = Response(
            status_code=403,
            data=json.loads(content.decode("utf-8"))
        )
