from datetime import date
from unittest import TestCase

from economic_dybdahl_rest.dto.customer import Customer
from economic_dybdahl_rest.dto.delivery import Delivery
from economic_dybdahl_rest.dto.line import Line
from economic_dybdahl_rest.dto.order import Order
from economic_dybdahl_rest.dto.payment_terms import PaymentTerms
from economic_dybdahl_rest.dto.recipient import Recipient


class TestOrder(TestCase):

    def test_to_dict(self):
        order = default_order


        expected = {
            "date": "2018-03-01",
            "currency": "DKK",
            "exchangeRate": 100,
            "netAmount": 10.00,
            "netAmountInBaseCurrency": 0.00,
            "grossAmount": 12.50,
            "marginInBaseCurrency": -46.93,
            "marginPercentage": 0.0,
            "vatAmount": 2.50,
            "roundingAmount": 0.00,
            "costPriceInBaseCurrency": 46.93,
            "paymentTerms": {
                "paymentTermsNumber": 1,
                "daysOfCredit": 14,
                "name": "Lobende maned 14 dage",
                "paymentTermsType": "net"
            },
            "customer": {
                "name": "28282828",
                "address": "Selma Lagerløftsvej",
                "city": "Aalborg Øst",
                "zipcode": "9220",
                "country": "Danmark",
                "currency": "DKK",
                "corporate_identification_number": "12345678",
                "customer_contact": "1",
                "ean": "28282828",
                "email": "Selma@Selma.dk",
                "p_number": "28282828",
                "vat_number": "28282828",
                "vat_zone_number": "28282828",
                "customer_number": "123",
                "attention": "1",
                "customerNumber": "123"
            },
            "recipient": {
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
            },
            "delivery": {
                "address": "Hovedvejen 1",
                "zip": "2300",
                "city": "Kbh S",
                "country": "Denmark",
                "deliveryDate": "2014-09-14"
            },
            "references": {
                "other": "aaaa"
            },
            "layout": {
                "layoutNumber": 5
            },
            "lines": [
                {
                    "unit": {
                        "unitNumber": 2,
                        "name": "Tim"
                    },
                    "product": {
                        "productNumber": "50"
                    },
                    "quantity": 1.00,
                    "unitNetPrice": 10.00,
                    "discountPercentage": 0.00,
                    "unitCostPrice": 46.93,
                    "totalNetAmount": 10.00,
                    "marginInBaseCurrency": -46.93,
                    "marginPercentage": 0.0
                }
            ]
        }
        self.assertDictEqual(expected, order.to_dict())

    def test_from_dict(self):
        pass

    def test_defaults_gets_set(self):
        order = Order(
            exchange_rate=100,
            net_amount=10.00,
            net_amount_in_base_currency=0.00,
            gross_amount=12.50,
            margin_in_base_currency=-46.93,
            margin_percentage=0.0,
            vat_amount=2.50,
            rounding_amount=0.00,
            cost_price_in_base_currency=46.93,
            payment_terms=PaymentTerms(
                payment_terms_number=1,
                days_of_credit=14,
                name='Lobende maned 14 dage',
                payment_terms_type='net'
            ),
            customer=Customer(address="Selma Lagerløftsvej",
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
                name="28282828"),
            recipient=Recipient(
                name='Toj & Co Grossisten',
                address='Vejlevej 21',
                zip='7000',
                city='Fredericia',
                vat_zone_name='Domestic',
                vat_zone_number=1
            ),
            delivery=Delivery(
                address='Hovedvejen 1',
                zip='2300',
                city='Kbh S',
                country='Denmark',
                delivery_date='2014-09-14'
            ),
            references='aaaa',
            layout_number=5,
            lines=[
                Line(
                    unit_number=2,
                    unit_name='Tim',
                    product_number='50',
                    quantity=1.00,
                    unit_net_price=10.00,
                    discount_percentage=0.00,
                    unit_cost_price=46.93,
                    total_net_amount=10.00,
                    margin_in_base_currency=-46.93,
                    margin_percentage=0.0
                )
            ]
        )
        expected = date.today().strftime('%Y-%m-%d')
        self.assertEqual(expected, order.date)
        self.assertEqual('DKK', order.currency)


default_order = Order(
    date='2018-03-01',
    currency='DKK',
    exchange_rate=100,
    net_amount=10.00,
    net_amount_in_base_currency=0.00,
    gross_amount=12.50,
    margin_in_base_currency=-46.93,
    margin_percentage=0.0,
    vat_amount=2.50,
    rounding_amount=0.00,
    cost_price_in_base_currency=46.93,
    payment_terms=PaymentTerms(
        payment_terms_number=1,
        days_of_credit=14,
        name='Lobende maned 14 dage',
        payment_terms_type='net'
    ),
    customer=Customer(address="Selma Lagerløftsvej",
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
        name="28282828")
    ,
    recipient=Recipient(
        name='Toj & Co Grossisten',
        address='Vejlevej 21',
        zip='7000',
        city='Fredericia',
        vat_zone_name='Domestic',
        vat_zone_number=1
    ),
    delivery=Delivery(
        address='Hovedvejen 1',
        zip='2300',
        city='Kbh S',
        country='Denmark',
        delivery_date='2014-09-14'
    ),
    references='aaaa',
    layout_number=5,
    lines=[
        Line(
            unit_number=2,
            unit_name='Tim',
            product_number='50',
            quantity=1.00,
            unit_net_price=10.00,
            discount_percentage=0.00,
            unit_cost_price=46.93,
            total_net_amount=10.00,
            margin_in_base_currency=-46.93,
            margin_percentage=0.0
        )
    ]
)
