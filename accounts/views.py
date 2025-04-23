from django.shortcuts import render
from .serializers import UserAccountSerializers
from .models import UserAccount
from rest_framework import generics

# Create your views here.

class UserAccountCreateView(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializers  # Fixed typo here
