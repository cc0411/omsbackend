from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializer import SaltCmdInfoSerializer,SaltKeySerializer,MinionListSerializer
from rest_framework.pagination import  PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import MinionList,SaltCmdInfo,SaltKeyList
from assets.views import AssetsPagination
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MinionListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = MinionList.objects.all()
    serializer_class = MinionListSerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JSONWebTokenAuthentication,]
    #search_fields = ('minion_id', 'minion_status')
    #ordering_fields = ('ctime',)

class  SaltKeyViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = SaltKeyList.objects.all()
    serializer_class = SaltKeySerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JSONWebTokenAuthentication, ]

class SaltCmdInfoViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = SaltCmdInfo
    serializer_class = SaltCmdInfoSerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JSONWebTokenAuthentication, ]





