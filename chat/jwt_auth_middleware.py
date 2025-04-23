import os
from urllib.parse import parse_qs
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from rest_framework_simplejwt.backends import TokenBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class JWTAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Extract the token from the query string.
        query_string = scope.get("query_string", b"").decode("utf8")
        query_params = parse_qs(query_string)
        token = query_params.get("token", [None])[0]

        if token:
            try:
                token_backend = TokenBackend(
                    algorithm=settings.SIMPLE_JWT.get("ALGORITHM", "HS256")
                )
                validated_data = token_backend.decode(token, verify=True)
                user_id = validated_data.get("user_id")
                if user_id is not None:
                    user = await database_sync_to_async(User.objects.get)(id=user_id)
                    scope["user"] = user
                else:
                    scope["user"] = AnonymousUser()
            except Exception as e:
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()

        # Call the inner application with the updated scope, forwarding all parameters.
        await self.inner(scope, receive, send)
