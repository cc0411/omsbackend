# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Assets,HostGroup,BusinessUnit,IDC,RemoteUser

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostGroup
        fields = '__all__'

class IdcSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = '__all__'

class BusinessUnitSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField(allow_null=True)
    def get_group(self,row):
        group_obj = HostGroup.objects.all()
        ret =[]
        for item in group_obj:
            ret.append({'id': item.id, 'name': item.name})
        return ret
    class Meta:
        model = BusinessUnit
        fields = '__all__'
class AssetSerializer(serializers.ModelSerializer):
    idc = serializers.SlugRelatedField(queryset=IDC.objects.all(),slug_field='name',allow_empty=True,allow_null=True)
    group = serializers.SlugRelatedField(many=True, queryset=HostGroup.objects.all(), slug_field='name',allow_empty=True,allow_null=True)
    business_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(),slug_field='name',allow_empty=True,allow_null=True)
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


