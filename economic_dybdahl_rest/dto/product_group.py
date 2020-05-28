from economic_dybdahl_rest.dto._model import Model


class ProductGroup(Model):

    def __init__(self, product_group_number) -> None:
        self.product_group_number = product_group_number
        super().__init__()

    def to_dict(self):
        return {
            'productGroupNumber': self.product_group_number
        }

    @staticmethod
    def from_dict(_dict):
        return ProductGroup(
            product_group_number=_dict['productGroupNumber']
        )
