from dataclasses import dataclass
from http import HTTPStatus

from economic_dybdahl_rest.api.draft_invoices import GetDraftInvoice
from economic_dybdahl_rest.usecases._listener import Listener
from economic_dybdahl_rest.http.response import Response


class GetDraftInvoiceListener(Listener):
    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'Invoice': data
            }
        )


@dataclass
class GetDraftInvoiceRequest:
    draft_invoice_number: str


class GetDraftInvoiceUseCase:

    @staticmethod
    def get(request: GetDraftInvoiceRequest, listener: GetDraftInvoiceListener):
        response = GetDraftInvoice().get(request.draft_invoice_number)
        if response.ok:
            listener.on_success(response.json())
        else:
            listener.on_unknown_error(response.status_code, response.json())
