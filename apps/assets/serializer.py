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

class BusinessUnitSerializer3(serializers.ModelSerializer):
    parent_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(), slug_field='name', allow_empty=True,required=False,
                                               allow_null=True)
    class Meta:
        model = BusinessUnit
        fields = '__all__'
class BusinessUnitSerializer2(serializers.ModelSerializer):
    parent_level = BusinessUnitSerializer3(many =True,required=False)
    parent_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(), slug_field='name',allow_empty=True,allow_null=True,required=False)
    class Meta:
        model = BusinessUnit
        fields = '__all__'
class BusinessUnitSerializer(serializers.ModelSerializer):
    parent_level = BusinessUnitSerializer2(many =True,required=False)
    parent_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(), slug_field='name',allow_empty=True,allow_null=True,required=False)
    class Meta:
        model = BusinessUnit
        fields = '__all__'
    #def  validate(self, attrs):
    #    del attrs["parent_level"]
    #    print(attrs)
    #    return attrs#
class AssetSerializer(serializers.ModelSerializer):
    idc = serializers.SlugRelatedField(queryset=IDC.objects.all(),slug_field='name',allow_empty=True,allow_null=True)
    role = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name',allow_empty=True,allow_null=True)
    business_unit = serializers.SlugRelatedField(queryset=BusinessUnit.objects.all(),slug_field='name',allow_empty=True,allow_null=True)
    #business_unit = BusinessUnitSerializer(read_only=True)
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

from django.db.models import Q
class TreeBusinessUnitSerializer(serializers.ModelSerializer):
    assets = serializers.SerializerMethodField()
    parent_level = BusinessUnitSerializer2(many=True,read_only=True )
    def get_assets(self,obj):
        all_assets = Assets.objects.filter(Q(business_unit_id=obj.id)|Q(business_unit__parent_unit_id=obj.id)|Q(business_unit__parent_unit__parent_unit_id=obj.id))
        assets_serializer = AssetSerializer(all_assets,many=True,context={'request':self.context['request']})
        return assets_serializer.data
    class Meta:
        model = BusinessUnit
        fields = '__all__'

