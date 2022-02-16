from rest_framework import serializers
from .models import UserAppModel


class UserAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAppModel
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
