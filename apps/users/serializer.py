# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','name','email','mobile','image','is_superuser')
