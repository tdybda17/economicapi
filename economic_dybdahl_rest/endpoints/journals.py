from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_journals.get_jorunals_listener import GetJournalsListener
from economic_dybdahl_rest.usecases.get_journals.get_journals import GetJournalsUseCase


class JournalsEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        listener = GetJournalsListener()
        GetJournalsUseCase.get(listener)
        response = listener.get_response()

        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )
