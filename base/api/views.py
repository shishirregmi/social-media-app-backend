from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from itertools import chain

from .serializers import ChatSerializer, FriendSerializer, UserSerializer
from base.models import Chat
from django.contrib.auth.models import User


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChats(request,room):
    data = Chat.objects.filter(room=room)
    serializer = ChatSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addChats(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        serializer.errors
    return Response(serializer.data)

@api_view(['POST'])
def addUsers(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        serializer.errors
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFriends(request):
    friends = User.objects.all()
    serializer = UserSerializer(friends, many=True)
    return Response(serializer.data)
