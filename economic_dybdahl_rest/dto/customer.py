from economic_dybdahl_rest.dto._model import Model


class Customer(Model):

    def __init__(self, customer_number) -> None:
        self.customer_number = customer_number

    def to_dict(self):
        return {
            'customerNumber': self.customer_number
        }

    @staticmethod
    def from_dict(_dict):
        return Customer(
            customer_number=_dict['customer_number']
        )
