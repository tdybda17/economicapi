import time
from http import HTTPStatus

from economic_dybdahl_rest.api.get_draft_order import GetDraftOrderAPI
from economic_dybdahl_rest.api.get_draft_orders import GetDraftOrdersAPI
from economic_dybdahl_rest.api.get_products import GetProducts
from economic_dybdahl_rest.api.get_sent_order import GetSentOrderAPI
from economic_dybdahl_rest.api.get_sent_orders import GetSentOrdersAPI
from economic_dybdahl_rest.dto.draft_order_line import DraftOrderLine
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetDraftOrderLinesListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'lines': data
            }
        )

    def on_unknown_error(self, error):
        self.response = Response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            data={
                'detail': error
            }
        )

    def on_does_not_exist(self, error):
        self.response = Response(
            status_code=HTTPStatus.NOT_FOUND,
            data={
                'detail': error
            }
        )


class GetDraftOrderLinesUseCase:

    @staticmethod
    def get(listener=None):
        try:
            draft_orders_numbers, sent_order_numbers = get_all_sent_and_drafts_order_numbers()

            request_draft_orders_lines, model_draft_orders_lines = get_all_draft_orders_request_and_model_lines(
                draft_orders_numbers=draft_orders_numbers,
                sent_order_numbers=sent_order_numbers
            )

            product_numbers = get_all_product_numbers_from_lines(lines=request_draft_orders_lines)

            products = get_all_products_to_list(product_numbers=product_numbers)

            find_and_map_available_to_lines(
                model_draft_order_lines=model_draft_orders_lines, products=products
            )

        except DoesNotExistException as e:
            listener.on_does_not_exist(str(e))
            return
        except OnUnknownErrorException as e:
            listener.on_unknown_error(str(e))
            return

        draft_order_lines = DraftOrderLine.to_list_of_dicts_from_multiple(model_draft_orders_lines)

        listener.on_success(draft_order_lines)
        return draft_order_lines


def get_all_sent_and_drafts_order_numbers():
    draft_order_numbers = get_order_numbers(GetDraftOrdersAPI())
    sent_order_numbers = get_order_numbers(GetSentOrdersAPI())
    return draft_order_numbers, sent_order_numbers


def get_order_numbers(api):
    order_numbers = []
    next_page = None
    while True:
        order_response = api.get(next_page)
        check_status_is_succeeded(order_response)

        orders_json = order_response.json()
        pagination = orders_json['pagination']
        orders = orders_json['collection']

        find_and_add_order_numbers(orders, order_numbers)

        if len(order_numbers) > pagination['results']:
            break

        try:
            next_page = pagination['nextPage']
        except KeyError:
            break

    return order_numbers


def find_and_add_order_numbers(draft_orders, order_numbers_list):
    for draft_order in draft_orders:
        order_number = draft_order['orderNumber']
        order_numbers_list.append(order_number)


def get_all_draft_orders_request_and_model_lines(draft_orders_numbers, sent_order_numbers):
    request_draft_order_lines, model_draft_order_lines = get_order_and_model_order_lines(
        api=GetDraftOrderAPI(),
        order_numbers=draft_orders_numbers
    )
    request_sent_order_lines, model_sent_order_lines = get_order_and_model_order_lines(
        api=GetSentOrderAPI(),
        order_numbers=sent_order_numbers
    )
    return request_draft_order_lines + request_sent_order_lines, model_draft_order_lines + model_sent_order_lines


def get_order_and_model_order_lines(api, order_numbers):
    model_order_lines = []
    request_order_lines = []

    for draft_order_number in order_numbers:
        response = api.get(draft_order_number)
        check_status_is_succeeded(response)
        draft_order_json = response.json()
        for line in [a for a in draft_order_json['lines'] if 'product' in a]:
            request_order_lines.append(line)
            model_order_lines.append(DraftOrderLine(
                order_number=draft_order_number,
                economic_number=line['product']['productNumber'],
                amount=line['quantity'],
                available=None
            ))
    return request_order_lines, model_order_lines


def get_all_product_numbers_from_lines(lines):
    product_numbers = []
    for line in lines:
        product_number = line['product']['productNumber']
        product_numbers.append(product_number)
    return product_numbers


def get_all_products_to_list(product_numbers):
    products = []
    product_numbers_no_duplicates = set(product_numbers)
    amount_left = len(product_numbers_no_duplicates)
    while amount_left > 0:
        get_products_api = GetProducts()
        products_to_get = []
        for count, product_number in enumerate(product_numbers_no_duplicates):
            if count > 19:
                break
            products_to_get.append(product_number)
        product_numbers_no_duplicates = [item for item in product_numbers_no_duplicates if item not in products_to_get]

        response = get_products_api.get(products_to_get)
        check_status_is_succeeded(response)
        json_response = response.json()

        products.extend(json_response['collection'])

        amount_left = len(product_numbers_no_duplicates)

    return products


def find_and_map_available_to_lines(model_draft_order_lines, products):
    for draft_order_line in model_draft_order_lines:
        for product in products:
            if draft_order_line.economic_number == product['productNumber']:
                draft_order_line.available = product['inventory']['available']


def check_status_is_succeeded(response):
    if response.status_code == HTTPStatus.NOT_FOUND:
        raise DoesNotExistException(response.content)
    if not response.ok:
        raise OnUnknownErrorException(response.content)


class DoesNotExistException(RuntimeError):
    pass


class OnUnknownErrorException(RuntimeError):
    pass
