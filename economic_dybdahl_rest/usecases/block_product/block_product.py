import json

from economic_dybdahl_rest.api.get_product import GetProduct
from economic_dybdahl_rest.api.put_product import PutProduct
from economic_dybdahl_rest.dto.product import Product


class BlockProductUseCase:

    @staticmethod
    def block(product_number, listener):
        get_api = GetProduct()
        response = get_api.get(product_number)
        if response.status_code == 200:
            product = json.loads(response.content.decode('utf-8'))
            inventory = product['inventory']
            try:
                in_stock = int(inventory['inStock'])
                ordered_from_suppliers = int(inventory['orderedFromSuppliers'])
                ordered_by_customers = int(inventory['orderedByCustomers'])
                if in_stock == 0 and ordered_by_customers == 0 and ordered_from_suppliers == 0:
                    _product = Product.from_dict(product)
                    _product.barred = True
                    response = PutProduct().put(_product)
                    if response.status_code == 200:
                        listener.on_success()
                        return
                    else:
                        listener.on_unknown_error(response.status_code, response.content)
                        return
                else:
                    listener.on_product_in_stock()
                    return
            except ValueError:
                listener.on_unable_to_convert_to_int()
                return

        elif response.status_code == 404:
            listener.on_does_not_exist()
        else:
            listener.on_unknown_error(response.status_code, response.content)
