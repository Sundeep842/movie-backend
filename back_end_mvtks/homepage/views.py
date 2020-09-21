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

# Create your views here.

def home(request):
    a=Movies.objects.values('title','image','genre','city').distinct()
    serializer=MoviesSerializer(a,many=True)
    return JsonResponse(serializer.data,safe=False)

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
