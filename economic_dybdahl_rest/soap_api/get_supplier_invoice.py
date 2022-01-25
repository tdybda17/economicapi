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
