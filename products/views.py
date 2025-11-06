from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produto_list")
    else:
        form = ProductForm()
    return render(request, "products/form.html", {"form": form})

def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})
