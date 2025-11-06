from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list_api(request):
    queryset = Product.objects.all()
    return Response(queryset)
