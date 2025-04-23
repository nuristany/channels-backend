from rest_framework import serializers
from .models import ChannelCategory, Channel, Message, Conversation, ChannelMedia, CategoryMedia
from accounts.serializers import UserAccountSerializers

class ChannelMediaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        channel_id = self.context.get('channel_id')
        
        if channel_id:
            return ChannelMedia.objects.create(channel_id=channel_id, **validated_data)
  
        else:
            raise serializers.ValidationError("Either 'channel' or 'category' must be specified.")
    
    class Meta:
        model = ChannelMedia
        fields = '__all__'

class CategoryMediaSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        category_id = self.context.get('category_id')
        if category_id:
            return CategoryMedia.objects.create(category_id=category_id, **validated_data)
        raise serializers.ValidationError("A 'category_id' must be specified in the context.")
    
    class Meta:
        model = CategoryMedia  # Fixed typo: should be CategoryMedia, not ChannelMedia
        fields = '__all__'

class ChannelCategorySerializer(serializers.ModelSerializer):
    media = CategoryMediaSerializer(many=True, read_only=True)

    class Meta:
        model = ChannelCategory
        fields = ['id', 'name', 'description', 'media']

class ChannelSerializer(serializers.ModelSerializer):
    media = ChannelMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ['id', 'name', 'category', 'media']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserAccountSerializers()

    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Conversation
        fields = '__all__'
        