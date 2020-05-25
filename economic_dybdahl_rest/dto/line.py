from economic_dybdahl_rest.dto._model import Model


class Line(Model):

    def __init__(
            self,
            unit_number,
            unit_name,
            product_number,
            quantity,
            unit_net_price,
            discount_percentage,
            unit_cost_price,
            total_net_amount,
            margin_in_base_currency,
            margin_percentage
    ):
        self.unit_number = unit_number
        self.unit_name = unit_name
        self.product_number = product_number
        self.quantity = quantity
        self.unit_net_price = unit_net_price
        self.discount_percentage = discount_percentage
        self.unit_cost_price = unit_cost_price
        self.total_net_amount = total_net_amount
        self.margin_in_base_currency = margin_in_base_currency
        self.margin_percentage = margin_percentage
        super().__init__()

    def to_dict(self):
        return {
            "unit": {
                "unitNumber": self.unit_number,
                "name": self.unit_name
            },
            "product": {
                "productNumber": self.product_number
            },
            "quantity": self.quantity,
            "unitNetPrice": self.unit_net_price,
            "discountPercentage": self.discount_percentage,
            "unitCostPrice": self.unit_cost_price,
            "totalNetAmount": self.total_net_amount,
            "marginInBaseCurrency": self.margin_in_base_currency,
            "marginPercentage": self.margin_percentage
        }

    @staticmethod
    def from_dict(_dict):
        return Line(
            unit_number=_dict['unit']['unitNumber'],
            unit_name=_dict['unit']['name'],
            product_number=_dict['product']['productNumber'],
            quantity=_dict['quantity'],
            unit_net_price=_dict['unitNetPrice'],
            discount_percentage=_dict['discountPercentage'],
            unit_cost_price=_dict['unitCostPrice'],
            total_net_amount=_dict['totalNetAmount'],
            margin_in_base_currency=_dict['marginInBaseCurrency'],
            margin_percentage=_dict['marginPercentage']
        )
