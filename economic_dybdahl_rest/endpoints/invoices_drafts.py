from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
