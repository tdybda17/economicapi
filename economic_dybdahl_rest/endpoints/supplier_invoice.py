from http import HTTPStatus

from django.http import JsonResponse
from rest_framework.views import APIView

from economic_dybdahl_rest.soap_api.create_supplier_invoice import CreateSupplierInvoiceAPI, \
    CreateSupplierInvoiceAPIListener, CreateSupplierInvoiceAPIRequest, CreateSupplierInvoiceWithLinesAPIListener, \
    CreateSupplierInvoiceWithLinesAPIRequest, SupplierInvoiceLine
from economic_dybdahl_rest.soap_api.get_supplier_invoice import GetSupplierInvoiceAPI, GetSupplierInvoiceAPIListener


class SupplierInvoiceEndpoint(APIView):
    permission_classes = ()

    def post(self, request):
        listener = CreateSupplierInvoiceAPIListener()
        CreateSupplierInvoiceAPI().create_supplier_invoice(CreateSupplierInvoiceAPIRequest(
            creditor=request.data.get('creditor', None),
            invoice_nr=request.data.get('invoice_nr', '')
        ), listener=listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

    def get(self, request, id):
        listener = GetSupplierInvoiceAPIListener()
        GetSupplierInvoiceAPI().get_supplier_invoice(id, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)


class SupplierInvoiceWithLinesEndpoint(APIView):
    permission_classes = ()

    def post(self, request):
        listener = CreateSupplierInvoiceWithLinesAPIListener()
        CreateSupplierInvoiceAPI().create_supplier_invoice_with_lines(CreateSupplierInvoiceWithLinesAPIRequest(
            request.data.get('creditor', None),
            request.data.get('invoice_nr', ''),
            request.data.get('lines', None)
        ), listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)
