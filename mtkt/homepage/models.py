from django.db import models

# Create your models here.
class Movies(models.Model):
        title=models.CharField(max_length=100)
        genre=models.CharField(max_length=100)     
        theatre=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        image=models.CharField(max_length=100)
        seats=models.IntegerField(max_length=100)
        seatsFilled=models.IntegerField(max_length=100)
        showtimes=models.IntegerField(max_length=100)
        def __str__(self):
            return self.title

class Booked(models.Model):
        username=models.CharField(max_length=100)
        Booked=models.BooleanField(max_length=100)
        def __str__(self):
             return self.username



    
