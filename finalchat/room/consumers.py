import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Connect to websocket and create group chat_roomname
        """
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print("ChatConsumer group add")
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        print("ChatConsumer connect")
        print(f"Group Name: {self.room_group_name}")
        await self.accept()

    
    async def disconnect(self, close_code):
        """
        Disconnect from websocket
        """
        
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

     # Receive message from WebSocket
    async def receive(self, text_data):
        """
        Event listener, listens for new messages
        Takes message and saves it to SQLite database
        Afterwards send to the group and html handles display on its own
        """
        data = json.loads(text_data)
        
        message = data['message']
        username = data['username']
        room = data['room']
        print("ChatConsumer save message")
        print(f"{data} message from user")
        await self.save_message(username, room, message)

        print(f"ChatConsumer send message to group {self.room_group_name}")
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        print("ChatConsumer send message to websocket")
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)