from rest_framework import serializers
from .models import Product, Letter, Content

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ['id', 'product', 'date']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['letter', 'sender', 'receiver', 'letter_content', 'page']