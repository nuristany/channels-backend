# from rest_framework import serializers
# from .models import UserAccount

# class UserAccountSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = UserAccount
#         fields = ['id', 'email', 'first_name', 'last_name']

from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.conf import settings
from djoser.serializers import UserCreateSerializer
from django.template.loader import render_to_string
from .models import UserAccount

from .tasks import send_activation_email  # ✅ import the task

class CustomeUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        #activation_link = f"{settings.FRONTEND_URL}/activate/{uid}/{token}"
        activation_link = f"http://localhost:8000/accounts/activate/{uid}/{token}"
        html_message = render_to_string('email_activation.html',{
            'first_name': user.first_name,
            'activation_link': activation_link
        })

        email_body = f"Hi {user.first_name}, \n\nPlease activate your account:\n{activation_link}"
        subject = "Activation Email"

        # ✅ Send with Celery
        send_activation_email.delay(subject, email_body, user.email, html_message)

        return user
    