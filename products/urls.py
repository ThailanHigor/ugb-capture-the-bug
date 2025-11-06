from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/edit/", views.product_edit, name="product_edit"),
]
