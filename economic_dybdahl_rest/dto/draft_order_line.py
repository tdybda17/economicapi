from economic_dybdahl_rest.dto._model import Model


class DraftOrderLine(Model):

    def __init__(
            self,
            order_number,
            economic_number,
            amount,
            available
    ):
        self.order_number = order_number
        self.economic_number = economic_number
        self.amount = amount
        self.available = available
        super().__init__()

    def to_dict(self):
        return {
            'order_number': self.order_number,
            'economic_number': self.economic_number,
            'amount': self.amount,
            'available': self.available
        }

    @staticmethod
    def from_dict(_dict):
        return DraftOrderLine(
            order_number=_dict.get('order_number', ''),
            economic_number=_dict.get('productNumber', ''),
            amount=_dict.get('quantity', 0),
            available=_dict.get('available', 0)
        )

    @staticmethod
    def to_list_of_dicts_from_multiple(draft_order_lines):
        return [line.to_dict() for line in draft_order_lines]
