from economic_dybdahl_rest.dto._model import Model


class Delivery(Model):

    def __init__(self, address, zip, city, country, delivery_date) -> None:
        self.address = address
        self.zip = zip
        self.city = city
        self.country = country
        self.delivery_date = delivery_date
        super().__init__()

    def to_dict(self):
        return {
            "address": self.address,
            "zip": self.zip,
            "city": self.city,
            "country": self.country,
            "deliveryDate": self.delivery_date
        }

    @staticmethod
    def from_dict(_dict):
        return Delivery(
            address=_dict['address'],
            zip=_dict['zip'],
            city=_dict['city'],
            country=_dict['country'],
            delivery_date=_dict['deliveryDate']
        )
