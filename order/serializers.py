from rest_framework import serializers
from .models import Customer, Order
from letter.serializers import LetterSerializer

class CustomerSerializer(serializers.ModelSerializer):
    #letter = LetterSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['letter', 'senderName', 'senderPhone', 'senderAddr', 'receiver', 'receiverPhone', 'receiverAddr', 'send_mail']

class OrderSerializer(serializers.ModelSerializer):
    #customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'letterName', 'letterPrice', 'letterPage_count', 'photo_price', 'send_mail', 'total_price', 'created_date']

