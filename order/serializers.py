from rest_framework import serializers
from .models import Customer, Order
from letter.serializers import LetterSerializer

class CustomerSerializer(serializers.ModelSerializer):
    letter = LetterSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['letter', 'senderName', 'senderPhone', 'sender_addr', 'receiver', 'receiver_phone_number', 'receiver_addr', 'send_mail']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'price']

