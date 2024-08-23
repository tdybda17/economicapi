from django.views import View
from rest_framework.permissions import IsAuthenticated


class OrderEndpoint(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        pass