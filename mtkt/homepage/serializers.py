from rest_framework import serializers


from .models  import Booked,Movies

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booked
        fields=('username','Booked')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields=('title','genre',
        'theatre',
        'city',
        'image',
        'seats','seatsFilled',
        'showtimes')