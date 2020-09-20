from django.shortcuts import render
from django.http.response import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from homepage.models import Booked,Movies
from .serializers import BookedSerializer,MovieSerializer
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    q= Booked.objects.all()
    serializer=BookedSerializer(q,many=True)
    return JsonResponse(serializer.data,safe=False)
def movie_list(request):
    b= Movies.objects.all()
    serializer=MovieSerializer(b,many=True)
    return JsonResponse(serializer.data,safe=False)
def  movie_city_list(request):
    z= Movies.objects.all()
    z =z.filter(city__icontains='pune')

    serializer=MovieSerializer(z,many=True)
    return JsonResponse(serializer.data,safe=False)




