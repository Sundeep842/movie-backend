from rest_framework import serializers 
from homepage.models import Movies,Booked
 
 
class MoviesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Movies
        fields = '__all__'

class BookedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Booked
        fields = '__all__'
