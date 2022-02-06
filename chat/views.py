from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
import django

from . import serializers

# from rest_framework.views import APIView

# Create your views here.

# Chat
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'csrf_token': django.middleware.csrf.get_token(request)
    })

# Registeration
@api_view(['POST'])
def register(request):
    if request.method == 'POST':

        data = dict()

        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            acc = serializer.save()
            data['response'] = 'Account created successfully!'
            data['username'] = acc.username
            data['token'] = Token.objects.get(user=acc).key

            return Response(data, status=status.HTTP_201_CREATED)
        
        data['response'] = 'Error: ' + str(serializer.errors)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"response": "Logout Successful"}, status=status.HTTP_200_OK)
    return Response({"response": "Error: Invalid request"}, status=status.HTTP_400_BAD_REQUEST)