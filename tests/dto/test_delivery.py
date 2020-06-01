from unittest import TestCase

from economic_dybdahl_rest.dto.delivery import Delivery


class TestDelivery(TestCase):

    def test_to_dict(self):
        delivery = Delivery(
            address='Hovedvejen 1',
            zip='0000',
            city='city',
            country='Den',
            delivery_date='2020-04-04'
        )
        expected = {
            "address": "Hovedvejen 1",
            "zip": "0000",
            "city": "city",
            "country": "Den",
            "deliveryDate": "2020-04-04"
        }
        self.assertDictEqual(expected, delivery.to_dict())

    def test_from_dict(self):
        delivery = Delivery.from_dict({
            "address": "Hovedvejen 1",
            "zip": "0000",
            "city": "city",
            "country": "Den",
            "deliveryDate": "2020-04-04"
        })
        self.assertEqual('Hovedvejen 1', delivery.address)
        self.assertEqual('0000', delivery.zip)
        self.assertEqual('city', delivery.city)
        self.assertEqual('Den', delivery.country)
        self.assertEqual('2020-04-04', delivery.delivery_date)
