from django.shortcuts import render
from .models import Product, Letter, User, Topic
from photo.models import Photo
from .serializers import ProductSerializer, LetterSerializer, UserSerializer, TopicSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

# Create your views here.
class ProductList(APIView):
    """
    List all Product or create a new Product
    """
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            """
            #동일 값을 가진 사람은 동일 인물로 간주 할 것인가?
            if request.COOKIES.get('userID') is not None: #쿠키 값이 있을 때
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else: #쿠키 값이 없을 때
                #처음 사용하는 유저인지 구분
                try:
                    value = request.data.get("senderEmail")
                    item = User.objects.get(senderEmail=value)
                except ObjectDoesNotExist: #처음 사용하는 유저일 때
                    serializer.save()
                    item = User.objects.get(senderEmail=value)
                response = Response(serializer.data, status=status.HTTP_201_CREATED)
                c_val = str(item.id)
                response.set_cookie('userID', c_val)
                return response
            """
            #여기 밑 부분 주석 제거하면 됨

            try:
                value = request.data.get("senderEmail")
                item = User.objects.get(senderEmail=value)
            except ObjectDoesNotExist:  # 처음 사용하는 유저일 때
                serializer.save()
                item = User.objects.get(senderEmail=value)
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            c_val = str(item.id)
            response.set_cookie('userID', c_val)
            return response

            """
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            """
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
            """
                쿠키 값 재설정 추가
            """
            id = int(request.COOKIES.get('userID'))
            item = Letter.objects.filter(user=id).latest() #맨 첫번째 object 반환
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            c_val = str(item.id)
            response.set_cookie('userID', c_val)
            return response
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

    def delete(self, request, pk, format=None):
        letter = self.get_object(pk)
        photos = Photo.objects.filter(letter=letter)
        for p in photos:
            p.delete()
        with transaction.atomic():
            letter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TopicList(APIView):
    """
    List all Topic or create a new Topic
    """
    def get(self, request, format=None):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TopicDetail(APIView):
    """
    Retrieve, update or delete a Topic instance
    """
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        topic = self.get_object(pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
