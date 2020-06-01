from unittest import TestCase

from economic_dybdahl_rest.dto.recipient import Recipient


class TestRecipient(TestCase):

    def test_to_dict(self):
        recipient = Recipient(
            name='Toj & Co Grossisten',
            address='Vejlevej 21',
            zip='7000',
            city='Fredericia',
            vat_zone_name='Domestic',
            vat_zone_number=1
        )
        expected = {
            "name": "Toj & Co Grossisten",
            "address": "Vejlevej 21",
            "zip": "7000",
            "city": "Fredericia",
            "vatZone": {
                "name": "Domestic",
                "vatZoneNumber": 1,
                "enabledForCustomer": True,
                "enabledForSupplier": True
            }
        }
        self.assertDictEqual(expected, recipient.to_dict())

    def test_from_dict(self):
        recipient = Recipient.from_dict({
            "name": "Toj",
            "address": "Vej",
            "zip": "0000",
            "city": "City",
            "vatZone": {
                "name": "V",
                "vatZoneNumber": 1,
            }
        })
        self.assertEqual('Toj', recipient.name)
        self.assertEqual('Vej', recipient.address)
        self.assertEqual('0000', recipient.zip)
        self.assertEqual('City', recipient.city)
        self.assertEqual('V', recipient.vat_zone_name)
        self.assertEqual(1, recipient.vat_zone_number)
