from homepage.serializer import MoviesSerializer,BookedSerializer
from .forms import CreateUserForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from  django.contrib import messages 
from  django.contrib.auth import authenticate,logout,login 
from homepage.models import Movies,Booked
from rest_framework.decorators import api_view
from  django.contrib.auth.forms import UserCreationForm
import json
# Create your views here.

def home(request):
    if request.user.is_authenticated: 
        a=Movies.objects.values('title','image','genre','city').distinct()
        serializer=MoviesSerializer(a,many=True)
        context={'data':serializer.data}
        return render(request,'homepage.js',context)
        #return JsonResponse(serializer.data,safe=False)
    else:
        return redirect('login')

def movie_city(request):
        b=Movies.objects.filter(city="pune").values("title","image","genre").distinct()
        serializer=MoviesSerializer(b,many=True)
        context={'data':serializer.data}
        #return JsonResponse(serializer.data,safe=False)
        return render(request,'moviecity.js',context)


def  register(request):
    form =CreateUserForm()
    if request.method=="POST":
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,"Account was created  "+user)
                return redirect('login')
            else:
                messages.info(request,'could not validate')
    context={'form':form}
    return render(request,'register.html',context)
    

def loggingin(request):
        logout(request)
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password') 
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homepage') 
            else:
                messages.info(request,'username or password incorrect')
        context ={}      
        return render(request,'login.html',context)
def loggingout(request):
    logout(request)
    return redirect('logout') 

def book(request):
    return HttpResponse('Booked')