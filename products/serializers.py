from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    preco = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Product
        fields = ["name", "description", "preco", "active"]
