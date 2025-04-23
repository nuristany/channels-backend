from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class ChannelCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'
        
class Channel(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ChannelCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.channel}'

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.conversation}'

class ChannelMedia(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    icon = models.ImageField(upload_to='media/icons', null=True, blank=True)
    banner = models.ImageField(upload_to='media/banners', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            existing = ChannelMedia.objects.filter(pk=self.pk).first()
            if existing.icon and self.icon and existing.icon != self.icon:
                existing.icon.delete(save=False)
            
            if existing.banner and self.banner and existing.banner != self.banner:
                existing.banner.delete(save=False)
        return super().save(*args, **kwargs)

    def __str__(self):
        if self.channel:
            return f'Media for {self.channel.name}'
        
        elif self.category:
            return f'Media for {self.category.name}'
        return 'Unassigned media'

        
class CategoryMedia(models.Model):
    category = models.ForeignKey(ChannelCategory, on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    icon = models.ImageField(upload_to='icons', null=True, blank=True)
    banner = models.ImageField(upload_to='banners', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            existing = CategoryMedia.objects.filter(pk=self.pk).first()
            if existing.icon and self.icon and existing.icon != self.icon:
                existing.icon.delete(save=False)

            if existing.banner and self.banner and existing.banner != self.banner:
                existing.banner.delete(save=False)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        
        if self.category:
            return f'Media for {self.category.name}'
        return 'Unassigned media'
    