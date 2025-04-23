from rest_framework import serializers
from .models import UserAccount


class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount

        fields = ['id', 'email', 'first_name', 'last_name']
