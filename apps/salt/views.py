from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializer import SaltCmdInfoSerializer,SaltKeySerializer,MinionListSerializer
from .models import MinionList,SaltCmdInfo,SaltKeyList
from assets.views import AssetsPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from .salt_api import SaltAPI
# Create your views here.

salt = SaltAPI()
class MinionListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = MinionList.objects.all()
    serializer_class = MinionListSerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated,]
    search_fields = ('minion_id', 'ip','system_type','hostname')
    ordering_fields = ('ctime','minion_id','hostname','memory')

class  SaltKeyViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = SaltKeyList.objects.all()
    serializer_class = SaltKeySerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated, ]
    filter_fields =['certification_status',]

class SaltCmdInfoViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = SaltCmdInfo
    serializer_class = SaltCmdInfoSerializer
    pagination_class = AssetsPagination
    permission_classes = [IsAuthenticated, ]

from utils import create_saltminion
class RefreshSalt(APIView):
    def get(self,request):
        type =request.query_params.get('type')
        if type =='key':
            result = create_saltminion.saltkey_list()
        elif type =='minion':
            result = create_saltminion.minion_status()
        else:
            result = '更新错误,请稍后再次尝试'
        if result:
            res = {'status':True,'msg':'更新成功'}
        else:
            res = {'status':False,'msg':'更新错误,请稍后再次尝试'}

        return JsonResponse(res)

class  PingSaltView(APIView):
    def get(self,request):
        minion_id = request.query_params.get('minion_id')
        result =salt.test_api(tgt=minion_id)
        print(result['return'])
        if len(result['return'][0]):
            if result['return'][0][minion_id]:
                res ={'status':True,'msg':'minion-%s连接成功' %minion_id}
            else:
                res ={'status':False,'msg':'minion-%s连接失败' %minion_id}
        else:
            res = {'status':False,'msg':'This minionID not Found,please check it'}
        return JsonResponse(res)

class SaltKeyView(APIView):
    def get(self,request):
        type = request.query_params.get('type')
        minion_id = request.query_params.get('minion_id')
        if type =='delete':
            salt.saltkey_delete_api(tgt=minion_id)
            res = {'status':True,'msg':'%s删除成功' %minion_id}
        elif type =='add':
            salt.saltkey_accept_api(tgt=minion_id)
            res = {'status':True,'msg':'%s认证成功' %minion_id}
        elif type =='rejected':
            salt.saltkey_reject_api(tgt=minion_id)
            res = {'status':True,'msg':'%s已拒绝' %minion_id}
        else:
            res = {'status':False,'msg':'please choise type'}
        return JsonResponse(res)




