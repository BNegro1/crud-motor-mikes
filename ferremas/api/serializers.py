from rest_framework import serializers
from admin_dashboard.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['code', 'brand', 'name', 'price', 'stock']
