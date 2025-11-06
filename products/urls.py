from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_products, name="produto_list"),
    path("ativos/", views.active_products, name="produto_list"),
    path("<int:pk>/", views.product_detail, name="produto_list"),
]
