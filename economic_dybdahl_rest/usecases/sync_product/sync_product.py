from economic_dybdahl_rest.api.put_product import PutProduct
from economic_dybdahl_rest.dto.product import ProductValidationError


class SyncProductUseCase:

    @staticmethod
    def sync(product, listener):
        try:
            product.validate()
        except ProductValidationError as e:
            listener.on_validation_error(e)

        api = PutProduct()
        response = api.put(product)
        if response.status_code == 200:
            listener.on_success()
        elif response.status_code == 201:
            listener.on_product_created()
        elif response.status_code == 400:
            listener.on_schema_validation_error(response.content)
        elif response.status_code == 401:
            listener.on_not_authorized()
        elif response.status_code == 403:
            listener.on_forbidden(response.content)
        else:
            listener.on_unknown_error(response.status_code, response.content)
