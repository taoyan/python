
from .models import UserInfo
from rest_framework import serializers
class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'