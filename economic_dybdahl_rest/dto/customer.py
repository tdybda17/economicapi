from economic_dybdahl_rest.dto._model import Model


class Customer(Model):

    def __init__(self, customer_number, name=None, delivery_locations=[]) -> None:
        self.customer_number = customer_number
        self.name = name
        self.delivery_locations = delivery_locations

    def to_dict(self):
        _dict = {
            'customerNumber': self.customer_number
        }
        if self.name:
            _dict['name'] = self.name

        if self.delivery_locations:
            _dict['delivery_locations'] = [d.to_dict() for d in self.delivery_locations]
        return _dict

    @staticmethod
    def from_dict(_dict):
        return Customer(
            customer_number=_dict['customer_number'],
            name=_dict.get('name', None)
        )

    @staticmethod
    def from_response(response):
        return Customer(
            customer_number=response['customerNumber'],
            name=response['name']
        )
