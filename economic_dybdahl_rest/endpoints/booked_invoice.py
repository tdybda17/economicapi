from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_booked_invoice.get_booked_invoice import GetBookedInvoiceListener, \
    GetBookedInvoiceUseCase


class BookedInvoiceEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, booked_id):
        listener = GetBookedInvoiceListener()
        GetBookedInvoiceUseCase.get(booked_id, listener)

        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )
