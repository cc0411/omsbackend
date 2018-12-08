# -*- coding: utf-8 -*-

import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omsbackend.settings")
    import django
    django.setup()
    from cloud import tencentcloud_api
    cloud_api = tencentcloud_api.TencentCloudAPI()
    cloud_api.get_project()