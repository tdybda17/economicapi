from http import HTTPStatus

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.soap_api.create_supplier_invoice import CreateSupplierInvoiceAPI, \
    CreateSupplierInvoiceWithLinesAPIListener
from economic_dybdahl_rest.soap_api.get_supplier_invoice import GetSupplierInvoiceAPI, GetSupplierInvoiceAPIListener, \
    GetSupplierInvoiceWithLinesAPIListener


class SupplierInvoiceWithLinesEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        listener = CreateSupplierInvoiceWithLinesAPIListener()
        CreateSupplierInvoiceAPI().create_supplier_invoice_with_lines(
            creditor_nr=request.data.get('creditor', None),
            invoice_nr=request.data.get('comment', ''),
            lines=request.data.get('lines', None),
            listener=listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

    def get(self, request, id):
        listener = GetSupplierInvoiceWithLinesAPIListener()
        GetSupplierInvoiceAPI().get_supplier_invoice_with_lines(id, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)
