from django.urls import path

from api.views import MyView

urlpatterns = [
    path('page/', MyView.as_view(), name='my_view')
]
