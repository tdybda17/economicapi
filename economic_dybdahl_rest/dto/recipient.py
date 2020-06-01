from economic_dybdahl_rest.dto._model import Model


class Recipient(Model):

    def __init__(self, name, address, zip, city, vat_zone_name, vat_zone_number) -> None:
        self.name = name
        self.address = address
        self.zip = zip
        self.city = city
        self.vat_zone_name = vat_zone_name
        self.vat_zone_number = vat_zone_number
        super().__init__()

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "zip": self.zip,
            "city": self.city,
            "vatZone": {
                "name": self.vat_zone_name,
                "vatZoneNumber": self.vat_zone_number,
                "enabledForCustomer": True,
                "enabledForSupplier": True
            }
        }

    @staticmethod
    def from_dict(_dict):
        return Recipient(
            name=_dict['name'],
            address=_dict['address'],
            zip=_dict['zip'],
            city=_dict['city'],
            vat_zone_name=_dict['vatZone']['name'],
            vat_zone_number=_dict['vatZone']['vatZoneNumber']
        )
