from rest_framework import serializers
from .models import flight,flight_details,passenger_info,ticket_info,card_details
from django.contrib.auth.models import User

class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = flight
        fields = '__all__'
class flightDSerializer(serializers.ModelSerializer):
    class Meta:
        model = flight_details
        fields = '__all__'
class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = passenger_info
        fields = '__all__'
class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket_info
        fields = '__all__'
class cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = card_details
        fields = '__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')