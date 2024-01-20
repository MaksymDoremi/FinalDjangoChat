from rest_framework import serializers
from room.models import Message, Room
from django.contrib.auth.models import User

"""
Serializer for build-in models.User
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


"""
Custom serializers for API
"""
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'slug']


class MessageSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ['id', 'room', 'user', 'content', 'date_added']
