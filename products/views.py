from django.shortcuts import render

def index(request):
   context = {
        'products': Product.objects.all()
   }
   return render(request, 'products/index.html', context)
