from economic_dybdahl_rest.dto._model import Model


class DeliveryLocation(Model):

    def __init__(self, address, zip_code, city, country, sort_key, barred, delivery_location_number) -> None:
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.sort_key = sort_key
        self.barred = barred
        self.delivery_location_number = delivery_location_number
        super().__init__()

    def to_dict(self):
        return {
            'address': self.address,
            'zip_code': self.zip_code,
            'city': self.city,
            'country': self.country,
            'sort_key': self.sort_key,
            'delivery_location_number': self.delivery_location_number,
            'barred': self.barred
        }

    @staticmethod
    def from_dict(_dict):
        return DeliveryLocation(
            address=_dict.get('address', ''),
            zip_code=_dict.get('postalCode', ''),
            city=_dict.get('city', ''),
            country=_dict.get('country', ''),
            sort_key=_dict.get('sortKey', ''),
            barred=_dict.get('barred', ''),
            delivery_location_number=_dict.get('deliveryLocationNumber', '')
        )
