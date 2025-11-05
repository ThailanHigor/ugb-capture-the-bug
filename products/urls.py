from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('cadastrar/', views.create_product, name='create_product'), 
]
