from economic_dybdahl_rest.dto._model import Model


class DeliveryLocation(Model):

    def __init__(self, address, zip_code, city, country, sort_key, barred) -> None:
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.sort_key = sort_key
        self.barred = barred
        super().__init__()

    def to_dict(self):
        return {
            'address': self.address,
            'zip_code': self.zip_code,
            'city': self.city,
            'country': self.country,
            'sort_key': self.sort_key,
            'barred': self.barred
        }

    @staticmethod
    def from_dict(_dict):
        return DeliveryLocation(
            address=_dict['address'],
            zip_code=_dict['postalCode'],
            city=_dict['city'],
            country=_dict.get('country', None),
            sort_key=_dict['sortKey'],
            barred=_dict['barred']
        )
