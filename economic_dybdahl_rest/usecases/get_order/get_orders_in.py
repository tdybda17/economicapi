import json
from http import HTTPStatus

from economic_dybdahl_rest.api.get_draft_orders import GetDraftOrdersInAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api.get_order import GetOrderSOAPAPI
from economic_dybdahl_rest.usecases._listener import Listener


class GetOrdersInListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'Orders': json.loads(data.decode("utf-8"))
            }
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )

    def on_empty_soap_ids_list(self):
        self.response = Response(
            data={'message': 'Der blev ikke medsendt nogle soap ids'},
            status_code=HTTPStatus.BAD_REQUEST
        )


class GetOrdersInUseCase:

    @staticmethod
    def get(soap_ids: list, listener=None):
        if not soap_ids:
            listener.on_empty_soap_ids_list()
            return

        data_array = []
        order_numbers = []
        orders = []
        try:
            for soap_id in soap_ids:
                temp = {
                    'OrderHandle': {
                        'Id': soap_id
                    }
                }
                data_array.append(temp)

            soap_order_response = GetOrderSOAPAPI().get_orders(data_array)
            for soap in soap_order_response:
                order_numbers.append(soap.Number)

            next_page = None
            while True:
                rest_response = GetDraftOrdersInAPI().get(order_numbers, next_page)

                if not rest_response.ok:
                    listener.on_unknown_error(content=json.loads(rest_response.content.decode("utf-8")),
                                              status_code=rest_response.status_code)
                    return

                orders.extend(rest_response.json()['collection'])

                try:
                    next_page = rest_response.json()['pagination']['nextPage']
                except KeyError:
                    break

            listener.on_success(orders)
            return

        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
