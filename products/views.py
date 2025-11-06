from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'GET'])
def products_api(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)  # parece não estar retornando erro se inválido
    else: 
        products = Product.objects.all()
        serializer = ProductSerializer(products) # deveria retornar muitos
        return Response(serializer.data)
