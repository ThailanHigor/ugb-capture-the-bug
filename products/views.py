from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        response = redirect("produto_list")
        form.save()
        return response
    return render(request, "products/form.html", {"form": form})


def list_products(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    return render(request, "products/list.html", {"products": products})
