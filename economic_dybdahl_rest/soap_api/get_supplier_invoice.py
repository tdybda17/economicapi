from economic_dybdahl_rest.dto.supplier_invoice import SupplierInvoice
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api._soap_api import EconomicSOAPApi
from economic_dybdahl_rest.usecases._listener import Listener


class GetSupplierInvoiceAPIListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            data={
                'id': data.Id,
                'creditor_nr': data.CreditorHandle.Number,
                'invoice_nr': data.InvoiceNo
            },
            status_code=200
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class GetSupplierInvoiceWithLinesAPIListener(Listener):

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


class GetSupplierInvoiceAPI(EconomicSOAPApi):

    def get_supplier_invoice(self, id, listener=GetSupplierInvoiceAPIListener()):
        try:
            response = self.client.service.CurrentSupplierInvoice_GetData(entityHandle={
                'Id': id
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        listener.on_success(response)
        return response

    def get_supplier_invoice_with_lines(self, id, listener=GetSupplierInvoiceWithLinesAPIListener()):
        try:
            supplier_invoice_data = self.client.service.CurrentSupplierInvoice_GetData(entityHandle={
                'Id': id
            })
            invoice_id = supplier_invoice_data.Id
            creditor_nr = supplier_invoice_data.CreditorHandle.Number
            invoice_nr = supplier_invoice_data.InvoiceNo

            line_nrs = self.client.service.CurrentSupplierInvoice_GetLines(currentSupplierInvoiceHandle={
                'Id': invoice_id
            })
            lines_data = self.client.service.CurrentSupplierInvoiceLine_GetDataArray(entityHandles={
                'CurrentSupplierInvoiceLineHandle': line_nrs
            })

            lines = []
            for line in lines_data:
                temp = {
                    "line_nr": line.Number,
                    "product_nr": line.ProductHandle.Number,
                    "amount": line.Quantity,
                    "price": line.UnitPrice
                }
                lines.append(temp)
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        invoice = SupplierInvoice(
            supplier_nr=creditor_nr,
            comment=invoice_nr,
            lines=lines,
            invoice_id=invoice_id
        )
        listener.on_success(invoice.to_dict(lines_has_line_number=True))
        return invoice.to_dict()
