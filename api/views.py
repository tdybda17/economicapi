from django.shortcuts import render

# Create your views here.
from django.views import View


class MyView(View):

    def get(self, request):
        context = {
            'page': 'mypage-title'
        }
        return render(request, 'mypage.html', context=context)
