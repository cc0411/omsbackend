# -*- coding: utf-8 -*-
from .models import  Region,Zone,Image,Instances,Project,InstancesType

import xadmin

class ProjectAdmin(object):
    list_display =['proid','proname','ctime']
    search_fields =['proid','proname','ctime']
    list_filter =['proid','proname','ctime']


class RegionAdmin(object):
    list_display =['region','name','state','utime']
    search_fields =['region','name','state','utime']
    list_filter =['region','name','state','utime']

class ZoneAdmin(object):
    list_display =['zid','region','zone','name','state','utime']
    search_fields = ['zid','region','zone','name','state','utime']
    list_filter = ['zid','region','zone','name','state','utime']

class ImageAdmin(object):
    list_display = ['region','imageid','os','size','name','des','init']
    search_fields = ['imageid','os','name','init']
    list_filter = ['imageid','os','name','init']


class InstancesAdmin(object):
    list_display=['placement','project','instance_id','instancestate','type','nip','wip','securityid','os','ctime','etime']
    search_fields =['placement','project','instance_id','os','ctime','etime','nip','wip']
    list_filter =['placement','project','instance_id','os','ctime','etime','nip','wip']


class InstanceTypeAdmin(object):
    list_display =['region','zone','family','type','cpu','memory']
    search_fields =['region','zone','family','type']
    list_filter =['region','zone','family','type']

xadmin.site.register(Project,ProjectAdmin)
xadmin.site.register(Zone,ZoneAdmin)
xadmin.site.register(Region,RegionAdmin)
xadmin.site.register(Image,ImageAdmin)
xadmin.site.register(Instances,InstancesAdmin)
xadmin.site.register(InstancesType,InstanceTypeAdmin)