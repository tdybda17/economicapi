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
    ):
        self.bar_code = bar_code
        self.cost_price = cost_price
        self.description = description
        self.name = name
        self.product_group = product_group
        self.product_number = product_number
        self.recommended_price = recommended_price
        self.sales_price = sales_price
        super().__init__()

    def to_dict(self):
        return {
            'barCode': self.bar_code,
            'costPrice': self.cost_price,
            'description': self.description,
            'name': self.name,
            'productGroup': self.product_group.to_dict(),
            'productNumber': self.product_number,
            'recommendedPrice': self.recommended_price,
            'salesPrice': self.sales_price
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
            sales_price=_dict['salesPrice']
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
            sales_price=request.POST.get('sale_price')
        )
