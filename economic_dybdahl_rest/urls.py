from django.urls import path

from economic_dybdahl_rest.endpoints.block_product import BlockProductEndpoint
from economic_dybdahl_rest.endpoints.product import ProductEndpoint

urlpatterns = [
    path('v1/product/', ProductEndpoint.as_view(), name='sync product endpoint'),
    path('v1/product/<str:product_number>/', ProductEndpoint.as_view(), name='product endpoint'),
    path('v1/product/<str:product_number>/block/', BlockProductEndpoint.as_view(), name='block product endpoint')
]
