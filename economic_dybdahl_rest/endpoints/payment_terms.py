from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.list_payment_terms.list_payment_terms import ListPaymentTermsListener, \
    ListPaymentTermsUseCase


class PaymentTermsEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        listener = ListPaymentTermsListener()
        ListPaymentTermsUseCase.list(listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )
