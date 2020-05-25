from django.urls import path

from economic_dybdahl_rest.endpoints.order import OrderEndpoint

urlpatterns = [
    path('v1/order/', OrderEndpoint.as_view(), name='order endpoint')
]
