from django.shortcuts import render
from .models import Product, Letter, User
from .serializers import ProductSerializer, LetterSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductList(APIView):
    """
    List all Product or create a new Product
    """
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    """
    test cookie
    """
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            """
            Add code
            """
            value = request.data.get("name")
            item = Product.objects.get(name=value)  # 현재 저장된 객체의 id 값을 가진 Product 객체 저장하고 싶은데!!!
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response.set_cookie('userID', item.name)
            return response
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    """
    Retrieve, update or delete a Product instance
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    """
    List all User or create a new User
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    #post 요청 시 cookie 설정 추가 해줘야함!
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LetterList(APIView):
    """
    List all Letter or create a new Letter
    """
    def get(self, request, format=None):
        letters = Letter.objects.all()
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LetterDetail(APIView):
    """
    Retrieve, update or delete a Letter instance
    """
    def get_object(self, pk):
        try:
            return Letter.objects.get(pk=pk)
        except Letter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        letter = self.get_object(pk)
        serializer = LetterSerializer(letter)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        letter = self.get_object(pk)
        serializer = LetterSerializer(letter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




