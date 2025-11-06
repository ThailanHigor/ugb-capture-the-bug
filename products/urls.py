from django.urls import path
from . import views

urlpatterns = [
    path("api/products/", views.api_products_list, name="api_products_list"),
    path("api/products/create/", views.api_products_create, name="api_products_create"),
]
