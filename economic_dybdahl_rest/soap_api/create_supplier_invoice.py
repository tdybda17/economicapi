from dataclasses import dataclass

from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api._soap_api import EconomicSOAPApi
from economic_dybdahl_rest.usecases._listener import Listener


@dataclass
class CreateSupplierInvoiceAPIRequest:
    creditor: int


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


class CreateSupplierInvoiceAPI(EconomicSOAPApi):

    def create_supplier_invoice(self, request: CreateSupplierInvoiceAPIRequest,
                                listener=CreateSupplierInvoiceAPIListener()):
        creditor_nr = request.creditor
        try:
            response = self.client.service.CurrentSupplierInvoice_Create(creditorHandle={
                'Number': creditor_nr
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        listener.on_success(response)
        return response
