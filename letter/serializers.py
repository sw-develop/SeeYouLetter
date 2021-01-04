from rest_framework import serializers
from .models import Product, Letter, User, Topic
from django.db import transaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'senderEmail']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'content']

class LetterSerializer(serializers.ModelSerializer):
    #product = ProductSerializer(read_only=True)
    SelectedQuestions = TopicSerializer(many=True)

    class Meta:
        model = Letter
        fields = ['id', 'paper', 'user', 'SelectedQuestions', 'font', 'month', 'letter_content', 'page', 'photo_price']

        @transaction.atomic
        def create(self, validated_data):
            topics_data = validated_data.pop('SelectedQuestions')
            letter = super(LetterSerializer, self).create(validated_data)

            #Validates topics data and creates SelectedQuestions
            try:
                topic_objects = TopicSerializer(data=topics_data, many=True)
                topic_objects.is_valid(raise_exception=True)
                topics = topic_objects.save()
                letter.SelectedQuestions.add(topics) #add topics to letter
            except:
                raise serializers.ValidationError("topics not valid.")

            letter.save()

            return letter


