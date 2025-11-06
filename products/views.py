from django.shortcuts import render
from .models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def active_products(request):
    products = Product.objects.filter(active=True)
    return render(request, "products/list.html", {"products": products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "products/detail.html", {"product": product})
