from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import (
    ChannelCategoryView,
    ChannelView,
    ChannelMediaView,
    CategoryMediaView,
    ConversationByChannelView,
    MessageListView,
)

# 1) Main and nested routers
router = DefaultRouter()
router.register(r'channel-categories', ChannelCategoryView, basename='channel-category')
router.register(r'channels', ChannelView, basename='channels')

nested_router = NestedDefaultRouter(router, r'channels', lookup='channel')
nested_router.register(r'media', ChannelMediaView, basename='channel-media')

category_nested_router = NestedDefaultRouter(router, r'channel-categories', lookup='category')
category_nested_router.register(r'media', CategoryMediaView, basename='category-media')

urlpatterns = [
    # Router URLs (channel‐categories, channels, channels/:id/media, etc.)
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(category_nested_router.urls)),

    # 2) Get (or auto‐create) the Conversation for a given channel
    path(
        'channels/<int:channel_id>/conversation/',
        ConversationByChannelView.as_view(),
        name='conversation-by-channel'
    ),

    # 3) Fetch all messages for a specific conversation
    path(
        'messages/conversation/<int:conversation_id>/',
        MessageListView.as_view(),
        name='message-list-by-conversation'
    ),
]
