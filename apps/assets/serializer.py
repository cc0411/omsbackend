# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Assets,Tag,BusinessUnit,IDC,RemoteUser

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id","name","desc",'ctime']

class IdcSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = ["id","name","desc",'ctime']
class BusinessUnitSerializer(serializers.ModelSerializer):
    parent_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(), slug_field='name')
    class Meta:
        model = BusinessUnit
        fields = "__all__"
class AssetSerializer(serializers.ModelSerializer):
    idc = serializers.SlugRelatedField(queryset=IDC.objects.all(),slug_field='name')
    role = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name')
    business_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(),slug_field='name')
    #status = serializers.CharField(source='get_status_display')
    #server_type = serializers.CharField(source='get_server_type_display')
    #自定义字段
    #idc2 = serializers.SerializerMethodField()

    def get_idc2(self,row):
        idc_obj = IDC.objects.all()
        ret =[]
        for item in idc_obj:
            ret.append({'id':item.id,'name':item.name})
        return ret
    class Meta:
        model = Assets
        fields = "__all__"
        #depth =2




