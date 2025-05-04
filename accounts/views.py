from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.views import View
from django.http import JsonResponse
from .tokens import account_activation_token

User = get_user_model()

class ActivateUserEmailView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return JsonResponse({'message': 'Account activated successfully!'}, status=200)
        else:
            return JsonResponse({'error': 'Activation link is invalid or expired.'}, status=400)
