from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm


def list_product(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'produtos': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('list_product')
    else:
        form = ProductForm()
    return render(request, 'products/register.html', {'form': form})
