from economic_dybdahl_rest.api.delete_product import DeleteProductApi


class DeleteProductUseCase:

    @staticmethod
    def delete(product_number, listener):
        api = DeleteProductApi()
        response = api.delete(product_number)
        status_code = response.status_code
        if status_code == 204:
            listener.on_success()
        elif status_code == 404:
            listener.on_does_not_exist()
        elif status_code == 400:
            listener.on_product_in_use()
        elif status_code == 401:
            listener.on_not_authorized()
        else:
            listener.on_unknown_error(response.status_code, response.content)
