import json
from http import HTTPStatus

from economic_dybdahl_rest.api.get_draft_order import GetDraftOrderAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api.get_order import GetOrderSOAPAPI
from economic_dybdahl_rest.usecases._listener import Listener


class GetOrderListener(Listener):
    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'Order': json.loads(data.decode("utf-8"))
            }
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class GetOrderUseCase:

    @staticmethod
    def get(id, listener=None):
        try:
            soap_order_response = GetOrderSOAPAPI().get_order(id)
            order_number = soap_order_response.Number
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return

        rest_order_response = GetDraftOrderAPI().get(order_number)

        if not rest_order_response.ok:
            listener.on_unknown_error(content=json.loads(rest_order_response.content.decode("utf-8")),
                                      status_code=rest_order_response.status_code)
            return

        listener.on_success(data=rest_order_response.content)
