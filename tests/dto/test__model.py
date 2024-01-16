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
        customer = Customer(address="Selma Lagerløftsvej",
                            zipcode="9220",
                            city="Aalborg Øst",
                            country="Danmark",
                            currency="DKK",
                            corporate_identification_number="12345678",
                            customer_number="123",
                            ean="28282828",
                            email="Selma@Selma.dk",
                            p_number="28282828",
                            vat_number="28282828",
                            vat_zone_number="28282828",
                            attention="1",
                            customer_contact="1",
                            name="28282828",
                            payment_term_number=1,
                            e_invoice_disabled=False)

        expected = "{\"name\": \"28282828\", \"address\": \"Selma Lagerl\\u00f8ftsvej\", \"city\": \"Aalborg \\u00d8st\", \"zipcode\": \"9220\", \"country\": \"Danmark\", \"currency\": \"DKK\", \"corporate_identification_number\": \"12345678\", \"customer_contact\": \"1\", \"ean\": \"28282828\", \"email\": \"Selma@Selma.dk\", \"p_number\": \"28282828\", \"vat_number\": \"28282828\", \"vat_zone_number\": \"28282828\", \"customer_number\": \"123\", \"attention\": \"1\", \"customerNumber\": \"123\", \"paymentTermsNumber\": 1, \"eInvoiceDisabled\": false}"
        self.assertEqual(expected, customer.to_json())
