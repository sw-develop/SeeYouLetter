from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['letter', 'senderName', 'senderPhone', 'senderFullAddress', 'senderDetailedAddress', 'senderZoneCode', 'receiver', 'receiverPhone', 'receiverFullAddress', 'receiverDetailedAddress', 'receiverZoneCode', 'postMethod']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['customer', 'letterName', 'letterPrice', 'page_price', 'photo_price', 'postMethod', 'postMethod_price', 'total_price', 'created_date']

