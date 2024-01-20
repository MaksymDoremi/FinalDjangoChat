from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from room.models import Room, Message
from django.contrib.auth.models import User
from .serializers import RoomSerializer, UserSerializer, MessageSerializer
from django.db.models import Q


"""
API methods
"""
@api_view(["GET"])
def AllMessages(request, format=None):
    if request.user.is_authenticated:
        if request.method == "GET":
            messages = Message.objects.all()
            serializer = MessageSerializer(messages, many=True)
            return Response({"messages": serializer.data})
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response({"message": "User not authenticated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def AllMessagesByUsername(request, username, format=None):
    if request.user.is_authenticated:
        if request.method == "GET":
            messages = Message.objects.filter(
                user=User.objects.get(username=username))
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response({"message": "User not authenticated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def AllMessagesByRoom(request, room_name, format=None):
    if request.user.is_authenticated:
        if request.method == "GET":
            messages = Message.objects.filter(
                room=Room.objects.get(name=room_name))
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response({"message": "User not authenticated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def AllMessagesByWord(request, word, format=None):
    if request.user.is_authenticated:
        if request.method == "GET":
            messages = Message.objects.filter(Q(content__icontains=word))
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return Response({"message": "User not authenticated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

"""
Method for creating room
"""
@api_view(["POST"])
def create_room(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "bad request during creating room"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response({"message": "User not authenticated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)