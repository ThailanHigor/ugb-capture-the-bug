from django.urls import path
from . import views

urlpatterns = [
    path("not_authenticated/", views.not_authenticated, name="not_authenticated"),
    path("create/", views.create_product, name="produto_create"),
    path("<int:pk>/edit/", views.update_product, name="produto_edit"),
    path("", views.list_products, name="produto_list"),
]
