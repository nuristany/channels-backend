import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ChannelMedia, CategoryMedia

@receiver(pre_delete, sender=ChannelMedia)
def delete_channel_media(sender, instance, **kwargs):
    if instance.icon:
        instance.icon.delete(save=False)
    if instance.banner:
        instance.banner.delete(save=False)

@receiver(pre_delete, sender=CategoryMedia)
def delete_category_media(sender, instance, **kwargs):
    if instance.icon:
        instance.icon.delete(save=False)
    if instance.banner:
        instance.banner.delete(save=False)
