from rest_framework import serializers
from .models import Product, Letter

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ['id', 'product', 'sender_phone_number', 'date', 'sender', 'receiver', 'letter_content', 'page']

