import json

from economic_dybdahl_rest.api.get_product import GetProduct


class BlockProductUseCase:

    @staticmethod
    def block(product_number, listener):
        get_api = GetProduct()
        response = get_api.get(product_number)
        if response.status_code == 200:
            product = json.loads(response.content.decode('utf-8'))
        elif response.status_code == 404:
            listener.on_does_not_exist()
            return
        else:
            listener.on_unknown_error(response.status_code, response.content)
            return

