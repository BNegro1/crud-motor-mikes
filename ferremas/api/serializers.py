
from rest_framework import serializers
from admin_dashboard.models import Product, Order, Payment, Delivery

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'status', 'client_name', 'client_address', 'client_email']

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'status', 'payment_date']

class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Delivery
        fields = ['id', 'order', 'status', 'delivery_date']
