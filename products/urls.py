from django.urls import path
from . import views

urlpatterns = [
    path("api/products/", views.api_products, name="api_products"),
]
