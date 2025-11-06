from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def create_product(request):
    if request.method == "GET":
        form = ProductForm(request.POST)
        response = redirect("produto_list")
        if form.is_valid():
            form.save()
        return response
    else:
        form = ProductForm()
    return render(request, "products/form.html", {"form": form})