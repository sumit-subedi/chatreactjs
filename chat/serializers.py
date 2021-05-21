from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class messageSerializer(serializers.ModelSerializer):
    sent = UserSerializer(required=True)
    class Meta:
        model = message
        fields = ('sent','message')