from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/edit/", views.update_product, name="produto_edit"),
    path("", views.list_products, name="produto_list"),
]

