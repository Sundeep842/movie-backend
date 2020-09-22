from django.contrib import admin
from django.urls import path,include
from . import views 
#from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('register/',views.register),
    path('login/', views.loggingin, name="login"),
    path('homepage/', views.home,name='homepage'),
    path('logout/', views.loggingout,name='logout'),
    path('moviecity/', views.movie_city,name='homepage'),

]
