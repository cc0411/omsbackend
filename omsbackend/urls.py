"""omsbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from omsbackend.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import  include_docs_urls
from rest_framework.routers import DefaultRouter
#jwt使用
from rest_framework_jwt.views import obtain_jwt_token
from assets.views import AssetViewSet,IdcViewSet,BusinessUnitViewSet,RoleViewSet
from salt.views import MinionListViewSet,SaltCmdInfoViewSet,SaltKeyViewSet
from users.views import UserInfoViewSet
from django.views.generic import TemplateView
router = DefaultRouter()

#主机管理路由
router.register(r'assets',AssetViewSet,base_name='assets'),
router.register(r'idc',IdcViewSet,base_name='idc'),
router.register(r'role',RoleViewSet,base_name='role'),
router.register(r'businessunit',BusinessUnitViewSet,base_name='businessunit'),
#salt路由
router.register(r'minionlist',MinionListViewSet,base_name="minionlist")
router.register(r'saltkey',SaltKeyViewSet,base_name="saltkey")
router.register(r'cmdinfo',SaltCmdInfoViewSet,base_name="cmdinfo")
#用户个人信息
router.register(r'users',UserInfoViewSet,base_name="users")
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^xadmin/',include(xadmin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    #django默认认证
    url(r'^api-auth/', include('rest_framework.urls')),
    #rest文档页
    url(r'docs/',include_docs_urls(title="Vueshop")),
    #路由
    url(r'^api/', include(router.urls)),
    #jwt的认证接口,用于获取token   header加入Authorization: JWT <your_token>
    url(r'^login/$', obtain_jwt_token),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
