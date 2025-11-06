from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.salvar()
            return redirect("produto_list")
    else:
        form = ProductForm()
    return render(request, "products/form.html", {"form": form})
