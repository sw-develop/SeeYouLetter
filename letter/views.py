from django.shortcuts import render
from .models import Product, Letter
from .serializers import ProductSerializer, LetterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
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




