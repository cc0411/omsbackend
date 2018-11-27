from rest_framework import viewsets,mixins,generics
from .serializer import AssetSerializer,IdcSerializer,TagSerializer,BusinessUnitSerializer,UnitTreeSerializer
from rest_framework.pagination import  PageNumberPagination
from .models import Assets,IDC,HostGroup,BusinessUnit
from rest_framework.permissions import  IsAuthenticated
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
    filter_fields = ['status','server_type','business_unit','group']
    search_fields = ('wip','nip','status','hostname','desc','server_type')
    ordering_fields = ('ctime','hostname','wip','nip')
    permission_classes = (IsAuthenticated,)


class IdcViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IdcSerializer
    permission_classes = [IsAuthenticated, ]

class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, ]

class  BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = BusinessUnitSerializer
    permission_classes = [IsAuthenticated, ]

class  UnitTreeViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnit.objects.all()
    serializer_class = UnitTreeSerializer
    permission_classes = [IsAuthenticated, ]


