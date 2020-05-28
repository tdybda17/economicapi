from economic_dybdahl_rest.dto._model import Model
from datetime import date as _date


class Order(Model):

    def __init__(
            self,
            exchange_rate,
            net_amount,
            net_amount_in_base_currency,
            gross_amount,
            margin_in_base_currency,
            margin_percentage,
            vat_amount,
            rounding_amount,
            cost_price_in_base_currency,
            payment_terms,
            customer,
            recipient,
            delivery,
            references,
            layout_number,
            lines,
            currency='DKK',
            date=_date.today().strftime("%Y-%m-%d")
    ):
        self.date = date
        self.currency = currency
        self.exchange_rate = exchange_rate
        self.net_amount = net_amount
        self.net_amount_in_base_currency = net_amount_in_base_currency
        self.gross_amount = gross_amount
        self.margin_in_base_currency = margin_in_base_currency
        self.margin_percentage = margin_percentage
        self.vat_amount = vat_amount
        self.rounding_amount = rounding_amount
        self.cost_price_in_base_currency = cost_price_in_base_currency
        self.payment_terms = payment_terms
        self.customer = customer
        self.recipient = recipient
        self.delivery = delivery
        self.references = references
        self.layout_number = layout_number
        self.lines = lines

    def to_dict(self):
        return {
            "date": self.date,
            "currency": self.currency,
            "exchangeRate": self.exchange_rate,
            "netAmount": self.net_amount,
            "netAmountInBaseCurrency": self.net_amount_in_base_currency,
            "grossAmount": self.gross_amount,
            "marginInBaseCurrency": self.margin_in_base_currency,
            "marginPercentage": self.margin_percentage,
            "vatAmount": self.vat_amount,
            "roundingAmount": self.rounding_amount,
            "costPriceInBaseCurrency": self.cost_price_in_base_currency,
            "paymentTerms": self.payment_terms.to_dict(),
            "customer": self.customer.to_dict(),
            "recipient": self.recipient.to_dict(),
            "delivery": self.delivery.to_dict(),
            "references": {
                "other": self.references
            },
            "layout": {
                "layoutNumber": self.layout_number
            },
            "lines": [line.to_dict() for line in self.lines]
        }

    @staticmethod
    def from_dict(_dict):
        raise NotImplementedError()
