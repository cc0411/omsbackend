from django.shortcuts import render
from .tencentcloud_api import TencentCloudAPI
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.

api = TencentCloudAPI()
class RegionView(APIView):
    def get(self,request):
        result = api.get_region()
        return HttpResponse(result)


class ZoneView(APIView):
    def get(self,request):
        region = request.query_params.get('region')
        result = api.get_zone(region)
        return HttpResponse(result)





