from django.urls import path
from . import views

urlpatterns = [
    path("api/products/", views.products_list, name="api_products"),
]
