from django.urls import path
from .views import UserAccountCreateView

urlpatterns = [
    path('users', UserAccountCreateView.as_view(), name='user-account-create')
]