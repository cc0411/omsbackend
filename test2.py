# -*- coding: utf-8 -*-

import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omsbackend.settings")
    import django
    django.setup()
    #from cloud import tencentcloud_api
    #cloud_api = tencentcloud_api.TencentCloudAPI()
    #cloud_api.get_project()
    from omsbackend import settings
    from QcloudApi.qcloudapi import QcloudApi

    module = 'account'
    action = 'DescribeProject'
    action_params = {
        'Limnit':1
    }
    config = {
        'Region': '',
        'secretId':settings.SECRETID,
        'secretKey':settings.SECRETKEY,
        'method':'GET',
        'SignatureMethod':'HmacSHA1',

    }
    service = QcloudApi(module,config)
    print(service.generateUrl(action,action_params))
    result =service.call(action, action_params)
    import json
    ret=json.loads(result.decode('utf-8'))
    print(ret)