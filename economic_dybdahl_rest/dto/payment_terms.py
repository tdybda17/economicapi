from economic_dybdahl_rest.dto._model import Model


class PaymentTerms(Model):

    def __init__(self, payment_terms_number, days_of_credit, name, payment_terms_type) -> None:
        self.payment_terms_number = payment_terms_number
        self.days_of_credit = days_of_credit
        self.name = name
        self.payment_terms_number = payment_terms_number
        self.payment_terms_type = payment_terms_type
        super().__init__()

    def to_dict(self):
        return {
            "paymentTermsNumber": self.payment_terms_number,
            "daysOfCredit": self.days_of_credit,
            "name": self.name,
            "paymentTermsType": self.payment_terms_type
        }

    @staticmethod
    def from_dict(_dict):
        return PaymentTerms(
            payment_terms_number=_dict['paymentTermsNumber'],
            days_of_credit=_dict['daysOfCredit'],
            name=_dict['name'],
            payment_terms_type=_dict['paymentTermsType']
        )
