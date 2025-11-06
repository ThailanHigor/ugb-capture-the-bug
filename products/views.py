from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def active_products_api(request):
    products = list(Product.objects.all())
    try:
        products = products.filter()
    except Exception as e:
        return Response({"erro": str(e)})

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)