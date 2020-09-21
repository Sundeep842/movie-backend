from homepage.serializer import MoviesSerializer,BookedSerializer

from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from homepage.models import Movies,Booked
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse('hi')