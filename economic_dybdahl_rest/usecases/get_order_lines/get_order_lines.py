import time
from http import HTTPStatus

from economic_dybdahl_rest.api.get_draft_order import GetDraftOrderAPI
from economic_dybdahl_rest.api.get_draft_orders import GetDraftOrdersAPI
from economic_dybdahl_rest.api.get_products import GetProducts
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetDraftOrderLinesListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'products': data
            }
        )

    def on_unknown_error(self, error):
        self.response = Response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            data=error
        )

    def on_does_not_exist(self, error):
        self.response = Response(
            status_code=HTTPStatus.NOT_FOUND,
            data=error
        )


class GetDraftOrderLinesUseCase:

    @staticmethod
    def get(listener=None):
        try:
            draft_orders_numbers = []
            data = []

            GetDraftOrderLinesUseCase.get_all_order_drafts_order_numbers(draft_orders_numbers=draft_orders_numbers)

            draft_orders_lines = []
            product_numbers = []

            GetDraftOrderLinesUseCase.get_all_draft_orders_lines(
                draft_orders_numbers=draft_orders_numbers,
                lines=draft_orders_lines,
                data=data
            )

            GetDraftOrderLinesUseCase.get_all_product_numbers_from_lines(
                lines=draft_orders_lines,
                product_numbers=product_numbers
            )

            products = GetDraftOrderLinesUseCase.get_all_products_to_list(product_numbers=product_numbers)

            GetDraftOrderLinesUseCase.find_and_map_available_to_product(
                data=data, products=products
            )

        except DoesNotExistException as e:
            listener.on_does_not_exist(str(e))
            return
        except OnUnknownErrorException as e:
            listener.on_unknown_error(str(e))
            return

        listener.on_success(data)
        return data

    @staticmethod
    def find_and_add_order_numbers(draft_orders, order_numbers_list):
        for draft_order in draft_orders:
            order_number = draft_order['orderNumber']
            order_numbers_list.append(order_number)

    @staticmethod
    def get_all_order_drafts_order_numbers(draft_orders_numbers):
        get_draft_orders_api = GetDraftOrdersAPI()
        next_page = None
        while True:
            draft_orders_response = get_draft_orders_api.get(next_page)
            GetDraftOrderLinesUseCase.check_status_is_succeeded(draft_orders_response)

            draft_orders_json = draft_orders_response.json()
            pagination = draft_orders_json['pagination']
            draft_orders = draft_orders_json['collection']

            GetDraftOrderLinesUseCase.find_and_add_order_numbers(draft_orders, draft_orders_numbers)

            if len(draft_orders_numbers) > pagination['results']:
                break

            try:
                next_page = pagination['nextPage']
            except KeyError:
                break

    @staticmethod
    def get_all_draft_orders_lines(draft_orders_numbers, lines, data):
        get_draft_order_api = GetDraftOrderAPI()

        for draft_order_number in draft_orders_numbers:
            response = get_draft_order_api.get(draft_order_number)
            GetDraftOrderLinesUseCase.check_status_is_succeeded(response)
            draft_order_json = response.json()
            for line in draft_order_json['lines']:
                lines.append(line)
                data.append({
                    'order_number': draft_order_number,
                    'product_economic_number': line['product']['productNumber'],
                    'product_amount': line['quantity']
                })
            time.sleep(2)

    @staticmethod
    def get_all_product_numbers_from_lines(lines, product_numbers):
        for line in lines:
            product_number = line['product']['productNumber']
            product_numbers.append(product_number)

    @staticmethod
    def get_all_products_to_list(product_numbers):
        products = []
        get_products_api = GetProducts()
        product_numbers_no_duplicates = list(dict.fromkeys(product_numbers))
        amount_left = len(product_numbers_no_duplicates)
        while amount_left > 0:
            products_to_get = []
            for count, product_number in enumerate(product_numbers_no_duplicates):
                if count > 19:
                    break
                products_to_get.append(product_number)

            response = get_products_api.get(products_to_get)
            GetDraftOrderLinesUseCase.check_status_is_succeeded(response)
            json_response = response.json()
            products.append(json_response['collection'])
            amount_left -= 20
        [products] = products
        return products

    @staticmethod
    def check_status_is_succeeded(response):
        if response.status_code == HTTPStatus.NOT_FOUND:
            raise DoesNotExistException(response)
        if not response.ok:
            raise OnUnknownErrorException(response)

    @staticmethod
    def find_and_map_available_to_product(data, products):
        for d in data:
            for product in products:
                if d['product_economic_number'] == product['productNumber']:
                    d['available'] = product['inventory']['available']


class DoesNotExistException(RuntimeError):
    pass


class OnUnknownErrorException(RuntimeError):
    pass
