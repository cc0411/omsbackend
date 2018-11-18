from django.shortcuts import render
from rest_framework import viewsets,mixins,generics
from .serializer import AssetSerializer,IdcSerializer,TagSerializer,BusinessUnitSerializer
from rest_framework.pagination import  PageNumberPagination
from .models import Assets,IDC,Tag,BusinessUnit
from rest_framework.views import  APIView
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

class AssetsPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 10
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'page_size'

    # 获取URL参数中传入的页码key
    page_query_param = 'page'

    # 最大支持的每页显示的数据条数
    max_page_size = 500

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all().order_by("-ctime")
    serializer_class = AssetSerializer
    pagination_class = AssetsPagination
    filter_fields = ['status','server_type','business_unit']
    search_fields = ('wip','nip','status','hostname','desc','server_type')
    ordering_fields = ('ctime','hostname','wip','nip')
    permission_classes = (IsAuthenticated,)

class IdcViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IdcSerializer
    permission_classes = [IsAuthenticated, ]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, ]

class  BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = BusinessUnitSerializer
    permission_classes = [IsAuthenticated, ]

from django.http import HttpResponse
class  BusinessUnitTree(APIView):
    def get(self,request,*args,**kwargs):
        data = BusinessUnit.objects.all()
        json_list =[]
        for item in data:
            json_dict = {}
            json_dict["name"] = item.name
            json_dict["id"] = item.id
            json_dict["parent_unit_id"] =item.parent_unit_id

            json_list.append(json_dict)
            print(json_list)
        json_list2 =[]
        for item in json_list:
            for dic in json_list2:
                try:
                    if item['parent_unit_id'] == dic['id']:
                        dic['children'] = [({'label': item['name'], 'id': item["id"]})]
                        break
                    if item['parent_unit_id'] == dic['children']['id']:
                        dic['children']['children'] = [({'label': item['name'], 'id': item["id"]})]
                        break
                except Exception as  e:
                    pass
            else:
                json_list2.append({"label": item["name"], "id": item["id"], "children": {}})
        import json
        return HttpResponse(json.dumps(json_list2,),content_type='application/json')





