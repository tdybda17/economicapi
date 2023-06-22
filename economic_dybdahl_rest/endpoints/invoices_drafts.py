from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.api.book_draft_invoice import BookDraftInvoiceRequest
from economic_dybdahl_rest.usecases.book_draft_invoice.book_draft_invoice import BookDraftInvoiceListener, \
    BookDraftInvoiceUseCase
from economic_dybdahl_rest.usecases.invoices_drafts.invoices_drafts import PostInvoicesDraftsUseCase
from economic_dybdahl_rest.usecases.invoices_drafts.invoices_drafts_listerner import InvoicesDraftsListener


class InvoicesDraftEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, invoice):
        listener = InvoicesDraftsListener()
        PostInvoicesDraftsUseCase.post(invoice, listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )


class BookDraftInvoiceEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, draft_invoice_number):
        listener = BookDraftInvoiceListener()
        request_object = self.get_request_object(request, draft_invoice_number)
        BookDraftInvoiceUseCase.book(request_object, listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )


    def get_request_object(self, request, draft_invoice_number):
        return BookDraftInvoiceRequest(
            draft_invoice_number=draft_invoice_number
        )
