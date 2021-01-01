from rest_framework import serializers
from .models import Product, Letter, User, Topic

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'senderEmail']

class LetterSerializer(serializers.ModelSerializer):
    #product = ProductSerializer(read_only=True)

    class Meta:
        model = Letter
        fields = ['id', 'product', 'user', 'topics', 'date', 'letter_content', 'page', 'photo_price']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        field = ['id', 'content']