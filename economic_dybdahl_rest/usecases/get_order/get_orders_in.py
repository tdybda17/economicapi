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

    def on_soap_orders_error(self, content, status_code):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )

    def on_get_single_order_error(self, content, status_code):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class GetOrdersInUseCase:

    @staticmethod
    def get(soap_ids: list = None, listener=GetOrdersInListener()):

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

                try:
                    soap_order_response = GetOrderSOAPAPI().get_orders(data_array)

                except Exception as e:
                    if 'E06000' in str(e):
                        soap_order_response, soap_error, error_msg = get_all_existing_soap_orders_individually(soap_ids)
                        if soap_error:
                            listener.on_soap_orders_error(error_msg, HTTPStatus.BAD_REQUEST)
                            return
                    else:
                        listener.on_soap_orders_error(
                            'An error occured getting the soap orders, from the following soap ids: ' + str(
                                soap_ids) + '. Got the following error msg: ' + str(e),
                            HTTPStatus.BAD_REQUEST
                        )
                        return

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
                    rest_response_content = json.loads(rest_response.content.decode("utf-8"))

                    try:
                        if rest_response_content['errorCode'] == 'E06000':
                            continue
                    except KeyError:
                        pass

                    listener.on_get_single_order_error(
                        content='Error occurred when trying to get order with number: ' + str(
                            order_number) + ' Got the following error response from economic: ' + str(
                            rest_response_content),
                        status_code=rest_response.status_code)
                    return

                orders.append(rest_response.json())

            listener.on_success(orders)
            return

        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return


def get_all_existing_soap_orders_individually(soap_ids):
    soap_orders = []
    error = False
    error_msg = None

    for soap_id in soap_ids:
        try:
            soap_orders.append(GetOrderSOAPAPI().get_order(soap_id))
        except Exception as e:
            if 'E06000' in str(e):
                continue
            else:
                error = True
                error_msg = 'Error occurred trying to get soap order from soap id: ' + str(
                    soap_id) + ' Got the following error msg from economic: ' + str(e)

    return soap_orders, error, error_msg
