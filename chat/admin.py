from django.contrib import admin
from .models import ChannelCategory, Channel, Message, Conversation, ChannelMedia, CategoryMedia

# Register your models here.
admin.site.register(ChannelCategory)
admin.site.register(Conversation)
admin.site.register(Channel)
admin.site.register(ChannelMedia)
admin.site.register(Message)
admin.site.register(CategoryMedia)

