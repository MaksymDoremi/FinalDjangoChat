"""
URL configuration for finalchat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('api/messages/', views.AllMessages, name="all_messages"),
    path('api/messages/username/<str:username>', views.AllMessagesByUsername, name="all_messages_by_username"),
    path('api/messages/room/<str:room_name>', views.AllMessagesByRoom, name="all_messages_by_room"),
    path('api/messages/contains/<str:word>', views.AllMessagesByWord, name="all_messages_by_word"),
    path('api/create_room/', views.create_room, name="api_create_room")
]

urlpatterns = format_suffix_patterns(urlpatterns)