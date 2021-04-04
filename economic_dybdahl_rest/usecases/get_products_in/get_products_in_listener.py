import json

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetProductsInListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data={
                'products': json.loads(data.decode("utf-8"))['collection']
            }
        )

    def on_unknown_error(self, status_code, content):
        content_dict = json.loads(content.decode("utf-8"))
        content_dict['status_code'] = status_code
        self.response = Response(
            status_code=520,
            data=content_dict
        )

    def on_does_not_exist(self):
        raise NotImplementedError()

    def on_empty_product_number_list(self):
        self.response = Response(
            status_code=400,
            data={'message': 'No product_numbers are provided'}
        )
