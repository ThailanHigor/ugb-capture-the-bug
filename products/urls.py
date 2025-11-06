from django.urls import path
from . import views

urlpatterns = [
    path("api/products/active/", views.active_products_api, name="api_active_products"),
]
