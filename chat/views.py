from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import ChannelCategory, Channel, Message, CategoryMedia, ChannelMedia, Conversation
from .serializers import ChannelCategorySerializer, ChannelMediaSerializer, ChannelSerializer,\
 MessageSerializer, CategoryMediaSerializer, ConversationSerializer

class ChannelCategoryView(viewsets.ModelViewSet):
    # Use ModelViewSet instead of ViewSet for default CRUD actions
    permission_classes = [IsAuthenticated]
    queryset = ChannelCategory.objects.all()
    serializer_class = ChannelCategorySerializer

class ChannelView(viewsets.ModelViewSet):
    # Use ModelViewSet here for consistency
    permission_classes = [IsAuthenticated]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = super().get_queryset()
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

class ChannelMediaView(ModelViewSet):
    serializer_class = ChannelMediaSerializer

    def get_serializer_context(self):
        return {
            'channel_id': self.kwargs['channel_pk']
        }

    def get_queryset(self):
        return ChannelMedia.objects.filter(channel_id=self.kwargs['channel_pk'])

class CategoryMediaView(ModelViewSet):
    serializer_class = CategoryMediaSerializer

    def get_serializer_context(self):
        return {
            'category_id': self.kwargs['category_pk']
        }

    def get_queryset(self):
        return CategoryMedia.objects.filter(category_id=self.kwargs['category_pk'])

class MessageListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, conversation_id):
        # Fetch all messages for a specific conversation
        messages = Message.objects.filter(conversation_id=conversation_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConversationByChannelView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, channel_id):
        conversation, _ = Conversation.objects.get_or_create(
            channel_id=channel_id,
            defaults={'name': f'channel-{channel_id}'}
        )
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
