from django.urls import path

from economic_dybdahl_rest.endpoints.product import ProductEndpoint

urlpatterns = [
    path('v1/product/', ProductEndpoint.as_view(), name='sync product endpoint'),
]
