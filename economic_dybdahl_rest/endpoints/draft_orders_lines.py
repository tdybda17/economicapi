from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_order_lines.get_order_lines import GetDraftOrderLinesUseCase, \
    GetDraftOrderLinesListener


class DraftOrdersLinesEndpoint(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        listener = GetDraftOrderLinesListener()
        GetDraftOrderLinesUseCase.get(listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code,
        )
