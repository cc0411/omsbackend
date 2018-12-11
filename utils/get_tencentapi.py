# -*- coding: utf-8 -*-
import time
from cloud.models import Image,Zone,Region,Project,Instances,InstancesType
from cloud.tencentcloud_api import TencentCloudAPI
from django.db.models import Q
import logging
logger = logging.getLogger('omsbackend.views')

import json


def get_region():
    print('开始更新Region列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    response_data = cloud_api.get_region()
    response_data = json.loads(response_data)
    data_source = response_data['RegionSet']
    for r in data_source:
        region = r['Region']
        name = r['RegionName']
        state = r['RegionState']
        update_values ={'region':region,'name':name,'state':state,'utime':time.strftime('%Y年%m月%d日 %X')}
        Region.objects.update_or_create(region=region,
                                        defaults=update_values)
    print('Region列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True
def get_zone():
    print('开始更新Zone列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    region_list = Region.objects.values('region','id').exclude(Q(region='ap-shanghai-fsi')|Q(region='ap-shenzhen-fsi'))
    for i in region_list:
        region = i['region']
        response_data = cloud_api.get_zone(region)
        response_data = json.loads(response_data)
        data_source = response_data['ZoneSet']
        for k in data_source:
            zone = k['Zone']
            name = k['ZoneName']
            state = k['ZoneState']
            zid =k['ZoneId']
            update_values = {'region_id':i['id'],'zone':zone,'name':name,'state':state,'zid':zid,'utime':time.strftime('%Y年%m月%d日 %X')}
            Zone.objects.update_or_create(region_id=i['id'],
                                          zone=zone,
                                          defaults=update_values)
    print('Zone列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True

def get_images():
    print('开始更新Image列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    region_list = Region.objects.values('region', 'id').exclude(
        Q(region='ap-shanghai-fsi') | Q(region='ap-shenzhen-fsi'))
    for i in region_list:
        region = i['region']
        resonse_data = cloud_api.get_image(region)
        resonse_data = json.loads(resonse_data)
        data_source = resonse_data['ImageSet']
        for k in data_source:
            imageid = k['ImageId']
            os = k['OsName']
            size = k['ImageSize']
            type = k['ImageType']
            state = k['ImageState']
            source = k['ImageSource']
            name = k['ImageName']
            des = k['ImageDescription']
            init = k['IsSupportCloudinit']
            platform = k['Platform']
            arch = k['Architecture']
            update_values = {'region_id':i['id'],
                             'imageid':imageid,
                             'os': os,
                             'size': size,
                             'type': type,
                             'state':state,
                             'source' : source,
                             'name' : name,
                             'des' : des,
                             'init' : init,
                             'platform' : platform,
                             'arch' :arch,
                             'utime' : time.strftime('%Y年%m月%d日 %X')
                             }
            Image.objects.update_or_create(region_id=i['id'],
                                           imageid=imageid,
                                           defaults=update_values)
    print('Image列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True

def get_instancetype():
    print('开始更新InstancesType列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    region_list = Region.objects.values('region', 'id').exclude(
        Q(region='ap-shanghai-fsi') | Q(region='ap-shenzhen-fsi'))
    for i in region_list:
        region = i['region']
        response_data = cloud_api.get_instancesType(region)
        response_data = json.loads(response_data)
        data_source = response_data["InstanceTypeConfigSet"]
        for k in data_source:
            zone = k['Zone']
            family = k['InstanceFamily']
            type = k['InstanceType']
            cpu = k['CPU']
            memory =k['Memory']
            update_values ={'region_id':i['id'],
                            'zone' : zone,
                            'family':family,
                            'memory':memory,
                            'type':type,
                            'cpu' : cpu
                            }
            InstancesType.objects.update_or_create(region_id=i['id'],
                                                   zone = zone,
                                                   family=family,
                                                   type=type,
                                                   defaults=update_values
                                                   )
    print('InstanceType列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True



def get_instances():
    print('开始更新Instances列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    region_list = Region.objects.values('region', 'id').exclude(
        Q(region='ap-shanghai-fsi') | Q(region='ap-shenzhen-fsi'))
    for i in region_list:
        region = i['region']
        response_data = cloud_api.get_describeinstances(region)
        response_data = json.loads(response_data)
        data_source = response_data['InstanceSet']
        for k in data_source:
            instance_id = k['InstanceId']
            zone = k['Placement']['Zone']
            projectid = k['Placement']['ProjectId']
            instancestate = k['InstanceState']
            restrictstate = k['RestrictState']
            type = k['InstanceType']
            cpu = k['CPU']
            memory = k['Memory']
            chargetype =k['InstanceChargeType']
            name = k['InstanceName']
            systemdisk = k['SystemDisk']['DiskType']
            try:
                if k['DataDIsks'] =='null':
                    datadisk = ''
                else:
                    datadisk = k['DataDisks']['DiskType']
            except Exception as  e:
                datadisk = ''
            nip = k['PrivateIpAddresses'][0]
            wip = k['PublicIpAddresses'][0]
            bandwith = k['InternetAccessible']['InternetMaxBandwidthOut']
            securityid = k['SecurityGroupIds'][0]
            vip = k["VirtualPrivateCloud"]["VpcId"]
            imageid = k["ImageId"]
            os = k["OsName"]
            renewflag =k["RenewFlag"]
            ctime = k["CreatedTime"]
            etime = k["ExpiredTime"]
            update_values ={'region_id':i['id'],
                            'instance_id' : instance_id,
                            'placement':Zone.objects.get(zone=zone).name,
                            'project' : projectid,
                            'instancestate' :instancestate,
                            'securityid' : securityid,
                            'image' : Image.objects.filter(imageid=imageid).first().name,
                            'os' : os,
                            'chargetype':chargetype,
                            'renewflag' :renewflag,
                            'ctime': ctime,
                            'etime' :etime,
                            'bandwith' :bandwith,
                            'nip':nip,
                            'wip' :wip,
                            'datadisk' :datadisk,
                            'systemdisk' :systemdisk,
                            'name' : name,
                            'type' : type,
                            'cpu':cpu,
                            'memory' : memory,
                            'restrictstate' : restrictstate}
            Instances.objects.update_or_create(region_id=i['id'],
                                               instance_id = instance_id,
                                               defaults = update_values
                                               )
    print('Instances列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True

def  get_project():
    print('开始更新项目列表' + time.strftime('%Y年%m月%d日 %X'))
    cloud_api = TencentCloudAPI()
    response_data = cloud_api.get_project()
    response_data = json.loads(response_data)
    data_source = response_data['data']
    for k in data_source:
        projectid = k['projectId']
        projectname = k['projectName']
        projcetinfo =k['projectInfo']
        ctime = k['createTime']
        update_values = {'proid':projectid,'proname':projectname,'ctime':ctime,'desc':projcetinfo}
        Project.objects.update_or_create(proid=projectid,defaults=update_values)
    print('项目列表更新完成' + time.strftime('%Y年%m月%d日 %X'))
    return True