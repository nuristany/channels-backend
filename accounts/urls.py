from django.urls import path
from .views import ActivateUserEmailView

urlpatterns = [
    path('activate/<uidb64>/<token>/', ActivateUserEmailView.as_view(), name='activate'),
]
