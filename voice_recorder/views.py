from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import *





@api_view(['GET','POST'])
def home(request):
    if request.method == "GET":
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == "POST":
        serializer = RecordSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import status

@api_view(['POST'])
def upload(request):
    print(request.data)
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





