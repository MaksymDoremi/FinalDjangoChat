import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalchat.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddleware(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})
