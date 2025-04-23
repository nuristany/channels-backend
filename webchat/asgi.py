


import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings.development')
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', 'webchat.settings.development')
)


django_asgi_app = get_asgi_application()


from . import urls

# application = ProtocolTypeRouter({
#     'http': django_asgi_app,
#     'websocket': URLRouter(urls.websockets_urlpatterns)
# })


# routing.py



import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import MyConsumer
from chat.jwt_auth_middleware import JWTAuthMiddleware

# Ensure Django settings are loaded
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings.development')
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', 'webchat.settings.development')
)


# Get the ASGI application for HTTP requests
django_asgi_app = get_asgi_application()

# Define your WebSocket routing and JWT middleware
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": JWTAuthMiddleware(
        URLRouter([
            path("ws/chat/<str:channelId>/", MyConsumer.as_asgi()),
        ])
    ),
})
