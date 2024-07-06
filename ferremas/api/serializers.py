from rest_framework import serializers
from usuarios.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'brand', 'name', 'price', 'stock', 'category']
