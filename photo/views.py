from django.shortcuts import render
from .models import Photo
from letter.models import Letter
from .serializers import PhotoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Create your views here.
class PhotoList(APIView):
    """
    List all Photo or create a new Photo
    """
    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    #사진 추가 시 photo_price 업데이트
    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            with transaction.atomic():
                letterObj=Letter.objects.get(pk=request.data.get('letter'))
                letterObj.photo_price += 1000
                letterObj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class PhotoDetail(APIView):
    """
    Retrieve, update or delete a Photo instance
    """
    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)