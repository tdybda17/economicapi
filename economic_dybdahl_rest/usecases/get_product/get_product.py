from economic_dybdahl_rest.api.get_product import GetProduct


class GetProductUseCase:

    @staticmethod
    def get(product_number, listener):
        api = GetProduct()
        response = api.get(product_number)
        if response.status_code == 200:
            listener.on_success(response.content)
        elif response.status_code == 404:
            listener.on_does_not_exist()
        else:
            listener.on_unknown_error(response.status_code, response.content)
