from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import passengerSerializer,ticketSerializer,flightDSerializer,flightSerializer,cardSerializer,AdminSerializer
from .models import flight,flight_details,passenger_info,ticket_info,card_details
from rest_framework import permissions
import json

class flightViewSet(ModelViewSet):
    queryset = flight.objects.all()
    serializer_class = flightSerializer
    permissions_classes =(permissions.IsAuthenticatedOrReadOnly)
class flightDViewSet(ModelViewSet):
    queryset = flight_details.objects.all()
    serializer_class = flightDSerializer
class passengerViewSet(ModelViewSet):
    queryset = passenger_info.objects.all()
    serializer_class = passengerSerializer
class ticketViewSet(ModelViewSet):
    queryset = ticket_info.objects.all()
    serializer_class = ticketSerializer
class cardViewSet(ModelViewSet):
    queryset = card_details.objects.all()
    serializer_class = cardSerializer
class AdminViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    '''login(request, user)'''
    login_user = AdminSerializer(user).data
    print(login_user)
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    result = {'token':token.key,'id':login_user['id'], 'username':login_user['username']}
    return Response(result)
    '''return Response({'token': token.key},
                    status=HTTP_200_OK)'''

@csrf_exempt
@api_view(['GET', 'POST','DELETE'])
def flight_listAll(request): 
    if request.method == 'GET':
        data = flight.objects.all()
        serializers = flightSerializer(data, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
         serializer = flightSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def flight_detail(request):
    if request.method == 'GET':
        data = flight_detail.objects.all()
        serializers = flightDSerializer(data, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
         serializer = flightDSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET','PUT','DELETE'])
def flight_list(request, pk):
    try:
        data = flight.objects.get(flight_id=pk)
    except flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = flightSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = flightSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)