import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat.consumers import MyConsumer
from chat.jwt_auth_middleware import JWTAuthMiddleware

# Ensure correct settings are loaded
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', 'webchat.settings.development')
)

# Get ASGI app for HTTP
django_asgi_app = get_asgi_application()

# Define WebSocket routes
websocket_urlpatterns = [
    path("ws/chat/<str:channelId>/", MyConsumer.as_asgi()),
]

# Full ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": JWTAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    ),
})
