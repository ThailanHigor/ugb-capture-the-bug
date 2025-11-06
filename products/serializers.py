from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(source='discount', max_digits=8, decimal_places=2)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'active']
