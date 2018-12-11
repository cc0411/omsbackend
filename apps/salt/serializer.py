# -*- coding: utf-8 -*-

from .models import SaltCmdInfo,SaltKeyList,MinionList
from rest_framework import serializers


class MinionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinionList
        fields = "__all__"


class SaltKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltKeyList
        fields = "__all__"


class SaltCmdInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltCmdInfo
        fields = "__all__"

