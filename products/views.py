from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("produto_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/form.html", {"form": form})

def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})
