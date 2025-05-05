from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chat.consumers import MyConsumer
from django.http import JsonResponse 

urlpatterns = [
    path('', lambda request: JsonResponse({'message': 'Welcome to the API'})),
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



websockets_urlpatterns = [path('ws/<str:channelId>/', MyConsumer.as_asgi())]


#websockets_urlpatterns = [path('ws/test', MyConsumer.as_asgi())]
#websockets_urlpatterns = [path('ws/chat/<str:channelId>/', MyConsumer.as_asgi())]