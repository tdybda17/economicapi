from http import HTTPStatus

from django.http import JsonResponse
from rest_framework.views import APIView

from economic_dybdahl_rest.soap_api.create_supplier_invoice import CreateSupplierInvoiceAPI, \
    CreateSupplierInvoiceAPIListener, CreateSupplierInvoiceAPIRequest
from economic_dybdahl_rest.soap_api.get_supplier_invoice import GetSupplierInvoiceAPI, GetSupplierInvoiceAPIListener


class SupplierInvoiceEndpoint(APIView):
    permission_classes = ()

    def post(self, request):
        listener = CreateSupplierInvoiceAPIListener()
        CreateSupplierInvoiceAPI().create_supplier_invoice(CreateSupplierInvoiceAPIRequest(
            creditor=request.data.get('creditor', None)), listener=listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

    def get(self, request, id):
        listener = GetSupplierInvoiceAPIListener()
        GetSupplierInvoiceAPI().get_supplier_invoice(id, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

