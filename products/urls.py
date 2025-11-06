from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_product, name="produto_create"),
    path("", views.list_products, name="produto_list"),
]
