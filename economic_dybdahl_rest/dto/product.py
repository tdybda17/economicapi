from economic_dybdahl_rest.dto._model import Model
from economic_dybdahl_rest.dto.product_group import ProductGroup


class Product(Model):

    def __init__(
            self,
            bar_code,
            cost_price,
            description,
            name,
            product_group,
            product_number,
            recommended_price,
            sales_price,
            barred
    ):
        self.bar_code = bar_code
        self.cost_price = cost_price
        self.description = description
        self.name = name
        self.product_group = product_group
        self.product_number = product_number
        self.recommended_price = recommended_price
        self.sales_price = sales_price
        self.barred = barred
        super().__init__()

    def to_dict(self):
        return {
            'barCode': self.bar_code,
            'costPrice': self.cost_price,
            'barred': self.barred,
            'description': self.description,
            'name': self.name,
            'productGroup': self.product_group.to_dict(),
            'productNumber': self.product_number,
            'recommendedPrice': self.recommended_price,
            'salesPrice': self.sales_price,
            'inventory': {
                'recommendedCostPrice': self.cost_price
            }
        }

    @staticmethod
    def from_dict(_dict):
        return Product(
            bar_code=_dict['barCode'],
            cost_price=_dict['costPrice'],
            description=_dict['description'],
            name=_dict['name'],
            product_group=ProductGroup.from_dict(_dict['productGroup']),
            product_number=_dict['productNumber'],
            recommended_price=_dict['recommendedPrice'],
            sales_price=_dict['salesPrice'],
            barred=_dict['barred']
        )

    @staticmethod
    def from_request(request):
        return Product(
            bar_code=request.POST.get('ean', ''),
            cost_price=request.POST.get('cost_price', ''),
            description=request.POST.get('description', ''),
            name=request.POST.get('name', ''),
            product_group=ProductGroup(request.POST.get('company_group_number', 0)),
            product_number=request.POST.get('hash_value'),
            recommended_price=request.POST.get('sale_price'),
            sales_price=request.POST.get('sale_price'),
            barred=request.POST.get('barred', False)
        )

    def validate(self):
        if self.product_number is None:
            raise ProductValidationError('Hash value/product number is required')

        try:
            self.cost_price = float(self.cost_price)
        except ValueError:
            raise ProductValidationError('Cost price needs to be a number')

        try:
            self.sales_price = float(self.sales_price)
        except ValueError:
            raise ProductValidationError('Sale price needs to be a number')

        try:
            self.recommended_price = float(self.recommended_price)
        except ValueError:
            raise ProductValidationError('Recommended price should be a number')

        try:
            self.product_group.product_group_number = int(self.product_group.product_group_number)
        except ValueError:
            raise ProductValidationError('Product group needs to be an integer')


class ProductValidationError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
