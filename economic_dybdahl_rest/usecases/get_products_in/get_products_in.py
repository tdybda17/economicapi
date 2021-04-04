from economic_dybdahl_rest.api.get_products import GetProducts


class GetProductsInUseCase:

    @staticmethod
    def get(product_numbers: list, listener):
        if not product_numbers:
            listener.on_empty_product_number_list()
            return

        api = GetProducts()
        response = api.get(product_numbers)
        if response.status_code == 200:
            listener.on_success(response.content)
        else:
            listener.on_unknown_error(response.status_code, response.content)
