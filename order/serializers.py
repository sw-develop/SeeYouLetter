from rest_framework import serializers
from .models import Customer, Order
from letter.models import Letter

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['letter']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'price']

