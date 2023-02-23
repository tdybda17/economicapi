from economic_dybdahl_rest.dto._model import Model


class Customer(Model):

    def __init__(self, attention,
                 address,
                 city,
                 zipcode,
                 country,
                 currency,
                 corporate_identification_number,
                 customer_contact,
                 ean,
                 email,
                 p_number,
                 vat_number,
                 vat_zone_number,
                 customer_number,
                 name=None) -> None:
        self.customer_number = customer_number
        self.name = name
        self.attention = attention
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.country = country
        self.currency = currency
        self.corporate_identification_number = corporate_identification_number
        self.customer_contact = customer_contact
        self.ean = ean
        self.email = email
        self.p_number = p_number
        self.vat_number = vat_number
        self.vat_zone_number = vat_zone_number

    def to_dict(self):
        _dict = {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'zipcode': self.zipcode,
            'country': self.country,
            'currency': self.currency,
            'corporate_identification_number': self.corporate_identification_number,
            'customer_contact': self.customer_contact,
            'ean': self.ean,
            'email': self.email,
            'p_number': self.p_number,
            'vat_number': self.vat_number,
            'vat_zone_number': self.vat_zone_number,
            'customer_number': self.customer_number,
            'attention': self.attention,
            'customerNumber': self.customer_number
        }

        if "contacts" in self.__dict__:
            _dict['contacts'] = self.contacts

        if "delivery_locations" in self.__dict__:
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
            attention=response.get('attention', ''),
            name=response.get('name', ''),
            address=response.get('address', ''),
            city=response.get('city', ''),
            zipcode=response.get('zip', ''),
            country=response.get('country', ''),
            currency=response.get('currency', ''),
            corporate_identification_number=response.get('corporateIdentificationNumber', ''),
            customer_contact=response.get('customerContact', ''),
            ean=response.get('ean', ''),
            email=response.get('email', ''),
            p_number=response.get('pNumber', ''),
            vat_number=response.get('vatNumber', ''),
            vat_zone_number=response.get(response['vatZone']['vatZoneNumber'], None),
            customer_number=response.get('customerNumber', ''),
        )
