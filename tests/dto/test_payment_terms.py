from unittest import TestCase

from economic_dybdahl_rest.dto.payment_terms import PaymentTerms


class TestPaymentTerms(TestCase):

    def test_to_dict(self):
        terms = PaymentTerms(
            payment_terms_number=1,
            days_of_credit=14,
            name='Name',
            payment_terms_type='type'
        )
        expected = {
            "paymentTermsNumber": 1,
            "daysOfCredit": 14,
            "name": "Name",
            "paymentTermsType": "type"
        }
        self.assertDictEqual(expected, terms.to_dict())

    def test_from_dict(self):
        terms = PaymentTerms.from_dict({
            "paymentTermsNumber": 1,
            "daysOfCredit": 14,
            "name": "Name",
            "paymentTermsType": "type"
        })
        self.assertEqual(1, terms.payment_terms_number)
        self.assertEqual(14, terms.days_of_credit)
        self.assertEqual('Name', terms.name)
        self.assertEqual('type', terms.payment_terms_type)
