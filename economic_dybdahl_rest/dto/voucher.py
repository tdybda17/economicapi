from economic_dybdahl_rest.dto._model import Model


class Voucher(Model):

    def __init__(self,
                 amount,
                 account_id,
                 contra_account_id,
                 text,
                 accounting_year,
                 voucher_type,
                 currency,
                 journal_id):
        self.amount = amount
        self.account_id = account_id
        self.contra_account_id = contra_account_id
        self.text = text
        self.accounting_year = accounting_year
        self.voucher_type = voucher_type
        self.currency = currency
        self.journal_id = journal_id
        super().__init__()

    def to_dict(self):
        return {
            'amount': self.amount,
            'account_id': self.account_id,
            'contra_account_id': self.contra_account_id,
            'text': self.text,
            'accounting_year': self.accounting_year,
            'voucher_type': self.voucher_type,
            'currency': self.currency,
            'journal_id': self.journal_id,
        }
