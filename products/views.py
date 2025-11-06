from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm


def list_product(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'produtos': products})

def detail_product(request, product_id):
    product = get_object_or_404(Product, id=produto_id)
    return render(request, 'products/detail.html', {'produto': product})
