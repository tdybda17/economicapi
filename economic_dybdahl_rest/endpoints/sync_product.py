from django.http import JsonResponse
from django.views import View


class SyncProductEndpoint(View):

    def post(self, request):
        print(request)
        return JsonResponse(data={})
