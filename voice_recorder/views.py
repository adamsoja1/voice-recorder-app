from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import *

from django.core.files.storage import default_storage
from django.http import HttpResponse


from django.core.files.storage import default_storage
from django.urls import reverse
from rest_framework import serializers



@api_view(['GET'])
def home(request,id):
    record = Record.objects.all()
    serializer = RecordSerializer(record, many=True, context={'request': request})
    return Response(serializer.data)



