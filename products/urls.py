from django.urls import path
from .views import product_list_api

urlpatterns = [
    path("api/products/", product_list_api, name="api_product_list"),
]
