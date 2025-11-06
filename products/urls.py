from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('<int:product_id>/', views.detail_product, name='detail_product'), 
]
