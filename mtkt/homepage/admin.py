from django.contrib import admin

# Register your models here.
from .models import Movies,Booked


admin.site.register(Movies)
admin.site.register(Booked)