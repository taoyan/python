
from .models import *
from rest_framework import exceptions

from rest_framework.authentication import BaseAuthentication
class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("验证失败")
        else:
            return token_obj.user, token_obj.token