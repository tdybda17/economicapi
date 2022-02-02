
from economic_dybdahl_rest.dto.supplier_invoice import SupplierInvoice
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api._soap_api import EconomicSOAPApi
from economic_dybdahl_rest.usecases._listener import Listener


class CreateSupplierInvoiceAPIListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            data={'id': data},
            status_code=200
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class CreateSupplierInvoiceWithLinesAPIListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            data={'invoice': data},
            status_code=200
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class CreateSupplierInvoiceAPI(EconomicSOAPApi):

    def __init__(self) -> None:
        super().__init__()

    def create_supplier_invoice(self, creditor_nr, invoice_nr,
                                listener=CreateSupplierInvoiceAPIListener()):
        creditor_nr = creditor_nr
        invoice_nr = invoice_nr
        try:
            response = self.client.service.CurrentSupplierInvoice_CreateFromData(data={
                'Handle': {
                    'Id': 1
                },
                'Id': 1,
                'InvoiceNo': invoice_nr,
                'CreditorHandle': {
                    'Number': creditor_nr
                }
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        listener.on_success(response)
        return response

    def create_supplier_invoice_with_lines(self, creditor_nr, invoice_nr, lines,
                                           listener=CreateSupplierInvoiceWithLinesAPIListener()):
        creditor_nr = creditor_nr
        invoice_nr = invoice_nr
        lines = lines
        try:
            invoice_id = self.client.service.CurrentSupplierInvoice_CreateFromData(data={
                'Handle': {
                    'Id': 1
                },
                'Id': 1,
                'InvoiceNo': invoice_nr,
                'CreditorHandle': {
                    'Number': creditor_nr
                }
            })

            data_array = []

            for line in lines:
                temp = {
                    'Handle': {
                        'InvoiceId': invoice_id,
                        'Number': 1,
                    },
                    'InvoiceId': invoice_id,
                    'Number': 1,
                    'InvoiceHandle': {
                        'Id': invoice_id
                    },
                    'ProductHandle': {
                        'Number': line['product_nr']
                    },
                    'Quantity': line['amount'],
                    'UnitPrice': line['price']
                }

                data_array.append(temp)

            response = self.client.service.CurrentSupplierInvoiceLine_CreateFromDataArray(dataArray={
                'CurrentSupplierInvoiceLineData': data_array
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        invoice = SupplierInvoice(
            supplier_nr=creditor_nr,
            comment=invoice_nr,
            lines=lines,
            invoice_id=invoice_id
        )
        listener.on_success(invoice.to_dict())
        return response