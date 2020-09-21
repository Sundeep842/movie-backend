
# Create your models here.
from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    genre = models.CharField(max_length=20,blank=False, default='')
    theatre = models.CharField(max_length=70, blank=False, default='')
    image = models.IntegerField( blank=False, default='')
    city = models.CharField(max_length=70, blank=False, default='')
    seats = models.IntegerField( blank=False, default='')
    seatsfilled = models.IntegerField( blank=False, default='')
    showtime = models.IntegerField( blank=False, default='')



class Booked(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    user = models.CharField(max_length=20,blank=False, default='')
    booked = models.BooleanField(max_length=70, blank=False, default='')  
    
    
    
    
    
    
    
