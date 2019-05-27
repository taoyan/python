from django.shortcuts import render

# Create your views here.
from .models import UserInfo
from .serializer import UserInfoModelSerializer

from rest_framework import viewsets
class UserInfoModelView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoModelSerializer