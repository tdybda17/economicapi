import json
from http import HTTPStatus

from economic_dybdahl_rest.api.get_draft_order import GetDraftOrderAPI
from economic_dybdahl_rest.api.get_draft_orders import GetDraftOrdersInAPI, GetDraftOrdersAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api.get_order import GetOrderSOAPAPI
from economic_dybdahl_rest.usecases._listener import Listener


class GetOrdersInListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'orders': data
            }
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class GetOrdersInUseCase:

    @staticmethod
    def get(soap_ids: list = None, listener=None):

        data_array = []
        order_numbers = []
        orders = []
        try:
            if soap_ids:
                for soap_id in soap_ids:
                    temp = {
                            'Id': soap_id
                    }
                    data_array.append(temp)

                soap_order_response = GetOrderSOAPAPI().get_orders(data_array)
                for soap in soap_order_response:
                    order_numbers.append(str(soap.Number))
            else:
                next_page = None
                while True:
                    draft_orders_response = GetDraftOrdersAPI().get(next_page)

                    if not draft_orders_response.ok:
                        listener.on_unknown_error(content=json.loads(draft_orders_response.content.decode("utf-8")),
                                                  status_code=draft_orders_response.status_code)
                        return

                    for draft_order in draft_orders_response.json()['collection']:
                        order_numbers.append(draft_order['orderNumber'])

                    try:
                        next_page = draft_orders_response.json()['pagination']['nextPage']
                    except KeyError:
                        break


            for order_number in order_numbers:
                rest_response = GetDraftOrderAPI().get(order_number)

                if not rest_response.ok:
                    listener.on_unknown_error(content=json.loads(rest_response.content.decode("utf-8")),
                                              status_code=rest_response.status_code)
                    return

                orders.append(rest_response.json())

            listener.on_success(orders)
            return

        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
