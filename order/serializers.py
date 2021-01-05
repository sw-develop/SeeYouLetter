from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['letter', 'senderName', 'senderPhone', 'senderFullAddress', 'senderDetailedAddress', 'senderZoneCode', 'receiver', 'receiverPhone', 'receiverFullAddress', 'receiverDetailedAddress', 'receiverZoneCode', 'postMethod']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['customer', 'letterName', 'letterPrice', 'letterPage_count', 'photo_price', 'postMethod', 'total_price', 'created_date']

