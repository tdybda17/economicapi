from economic_dybdahl_rest.dto._model import Model


class SupplierInvoice(Model):

    def __init__(self, supplier_nr, comment, lines, invoice_id) -> None:
        self.supplier_nr = supplier_nr
        self.comment = comment
        self.lines = lines
        self.invoice_id = invoice_id
        super().__init__()

    def to_dict(self, lines_has_line_number=False):
        return {
            "invoice_id": self.invoice_id,
            "supplier_nr": self.supplier_nr,
            "comment": self.comment,
            "lines": [{
                "line_nr": line['line_nr'] if lines_has_line_number else count + 1,
                "product_nr": line['product_nr'],
                "amount": line['amount'],
                "price": line['price'],
            }for count, line in enumerate(self.lines)]
        }

    @staticmethod
    def from_dict(_dict):
        pass
