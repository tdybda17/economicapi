from unittest import TestCase

from economic_dybdahl_rest.dto._model import Model
from economic_dybdahl_rest.dto.customer import Customer


class TestModel(TestCase):

    def test_to_dict(self):
        with self.assertRaises(NotImplementedError):
            Model().to_dict()

    def test_from_dict(self):
        with self.assertRaises(NotImplementedError):
            Model.from_dict({})

    def test_to_json(self):
        customer = Customer(customer_number='50')
        expected = '{"customerNumber": "50"}'
        self.assertEqual(expected, customer.to_json())
