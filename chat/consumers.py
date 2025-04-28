from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.conf import settings
from accounts.serializers import UserAccountSerializers
import jwt  # If you are using JWT for authentication

User = get_user_model()

class MyConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = None
        self.user = None
        self.channel_group_name = None

    def connect(self):
        # Get the channel ID from the URL route
        self.channel_id = self.scope['url_route']['kwargs'].get('channelId', None)
        
        # Extract the token from the query parameters
        token = self.scope['query_string'].decode().split('=')[-1]  # Getting the token from ?token=...

        if not self.channel_id or not token:
            self.close()  # Close if no channelId or token is provided
            return

        try:
            # Validate the token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')

            if user_id is None:
                self.close()
                return

            self.user = User.objects.get(id=user_id)
        except jwt.ExpiredSignatureError:
            self.close()  # Token expired
            return
        except jwt.InvalidTokenError:
            self.close()  # Invalid token
            return
        
        # Construct the group name from the channel_id
        self.channel_group_name = f"channel_{self.channel_id}"

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.channel_group_name,
            self.channel_name
        )

        self.accept()

        # Send user info to the client
        user_data = UserAccountSerializers(self.user).data
        user_data["type"] = "user_info"
        self.send_json(user_data)

    def disconnect(self, close_code):
        # Leave group on disconnect
        if self.channel_group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.channel_group_name,
                self.channel_name
            )

    def receive_json(self, content):
        message_text = content.get('message')
        if not message_text:
            return

        try:
            # Fetch the channel by its ID
            channel = Channel.objects.get(id=self.channel_id)
        except Channel.DoesNotExist:
            self.send_json({'error': 'Invalid channel'})
            return

        # Get or create the conversation for the channel
        from .models import Conversation, Message, Channel
        conversation, _ = Conversation.objects.get_or_create(
            name=f"channel-{self.channel_id}",
            channel=channel  # Link the conversation to the channel
        )

        # Save the message
        new_message = Message.objects.create(
            conversation=conversation,
            sender=self.user,
            content=message_text
        )

        # Broadcast the message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.channel_group_name,
            {
                'type': 'chat.message',
                'new_message': {
                    'id': new_message.id,
                    'sender': UserAccountSerializers(self.user).data,
                    'content': new_message.content,
                    'timestamp': new_message.timestamp.isoformat(),
                }
            }
        )

    def chat_message(self, event):
        # Send the message back to the WebSocket
        self.send_json({
            'message': event['new_message']
        })
