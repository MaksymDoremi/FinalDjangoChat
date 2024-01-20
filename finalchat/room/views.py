from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from finalchat.serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
import requests

from .models import Room, Message


@login_required
def rooms(request):
	"""
	Retreive all rooms and render rooms.html
	"""
	rooms = Room.objects.all()

	return render(request, 'rooms.html', {'rooms':rooms})
    

@login_required
def room(request, slug):
	"""
	Render specific room
	"""
	room = Room.objects.get(slug=slug)
	messages = Message.objects.filter(room=room)	
	return render(request, 'room.html', {'room': room, 'messages': messages})

@login_required
def create_room(request):
	"""
	Accepts POST method and send request to the api/create_room/
	"""
	if request.method == "POST":
		print(request.POST)
		# build data
		data = {"name":request.POST["room_name"], "slug":request.POST["room_name"].lower()}
		#build url
		url = request.build_absolute_uri(reverse("api_create_room"))
	
		# get response from API
		response = requests.post(url, data=data)
		
		# handle the response
		if response.status_code == 201:
			rooms = Room.objects.all()
			return render(request, "rooms.html", {"success_message": "Room created", 'rooms':rooms})
		else:
			#return render(request, "homePage.html", {"error_message": response.json().get("error")})
			return HttpResponse(response)

    
        