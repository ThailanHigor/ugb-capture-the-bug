from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_products, name="produto_list"),
    path("create/", views.create_product, name="produto_create"),
]
