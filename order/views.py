from django.shortcuts import render
from .models import Customer, Order
from letter.models import Letter, Product
from .serializers import CustomerSerializer, OrderSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Create your views here.
class CustomerList(APIView):
    """
    List all Customer or create a new Customer
    """
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    #Customer 생성 시 Order 동시에 생성 처리
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            with transaction.atomic():
                customerObj = Customer.objects.get(pk=request.data.get('letter'))
                letterObj = Letter.objects.get(pk=request.data.get('letter'))
                prodObj = Product.objects.get(pk=letterObj.paper.id)
                letter_price = letterObj.price_of_letter()
                mail_price = customerObj.price_of_mail() #등기우편 시 1000원 추가
                order = Order(
                    customer=customerObj,
                    letterName=prodObj.name,
                    letterPrice=prodObj.price,
                    letterPage_count=letterObj.page,
                    photo_price=letterObj.photo_price,
                    postMethod=customerObj.postMethod,
                    total_price=letter_price+mail_price #최종가격
                )
                order.save()
            serializer = OrderSerializer(Order.objects.get(pk=request.data.get('letter')))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    """
    Retrieve, update or delete a Customer instance
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):
    """
    List all Order or create a new Order
    """
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    #수정할 것) post 요청 시 Order 객체 생성도 처리해줘야 함
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    """
    Retrieve, update or delete a Order instance
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)