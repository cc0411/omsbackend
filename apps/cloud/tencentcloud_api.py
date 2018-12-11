# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client,models
from omsbackend import settings
import requests
import time
import sys
import random
import ssl
import  urllib.parse

ssl._create_default_https_context = ssl._create_unverified_context

class TencentCloudAPI(object):
    def __init__(self,secretid=settings.SECRETID,secretkey=settings.SECRETKEY):
        self.secretid= secretid
        self.secretkey = secretkey
        self.hp = HttpProfile()
        self.cp = ClientProfile()
    #获取签名
    def get_cred(self):
        return  credential.Credential(self.secretid,self.secretkey)
    #获取项目
    def get_project(self,):
       try:
           from QcloudApi.qcloudapi import QcloudApi
           module = 'account'
           action = 'DescribeProject'
           action_params = {
               'Limnit': 1
           }
           config = {
               'Region': '',
               'secretId': self.secretid,
               'secretKey': self.secretkey,
               'method': 'GET',
               'SignatureMethod': 'HmacSHA1',
           }
           service = QcloudApi(module, config)
           #print(service.generateUrl(action, action_params))
           result = service.call(action, action_params)
           ret = result.decode('utf-8')
           return ret
       except Exception as e:
           pass


    #获取region
    def get_region(self):
        try:
            cred = self.get_cred()
            self.hp.endpoint = "cvm.tencentcloudapi.com"
            self.cp.httpProfile = self.hp
            client = cvm_client.CvmClient(cred,'',self.cp)
            req = models.DescribeRegionsRequest()
            params = '{}'
            req.from_json_string(params)
            resp = client.DescribeRegions(req)
            return resp.to_json_string()
        except TencentCloudSDKException as e:
            return None
    #获取region下的zone列表
    def get_zone(self,region):
        try:
            cred = self.get_cred()
            self.hp.endpoint = "cvm.tencentcloudapi.com"
            self.cp.httpProfile = self.hp
            client = cvm_client.CvmClient(cred,region,self.cp)
            req = models.DescribeZonesRequest()
            params = '{}'
            req.from_json_string(params)
            resp = client.DescribeZones(req)
            return resp.to_json_string()
        except TencentCloudSDKException as e:
            return None
    #获取region下的镜像列表
    def get_image(self,region):
        try:
            cred = self.get_cred()
            self.hp.endpoint = "cvm.tencentcloudapi.com"
            self.cp.httpProfile = self.hp
            client = cvm_client.CvmClient(cred,region,self.cp)
            req = models.DescribeImagesRequest()
            params = '{}'
            req.from_json_string(params)
            resp = client.DescribeImages(req)
            return resp.to_json_string()
        except TencentCloudSDKException as e:
            return None

    #获取实例机型
    def get_instancesType(self,region):
        try:
            cred = self.get_cred()
            self.hp.endpoint = "cvm.tencentcloudapi.com"
            self.cp.httpProfile = self.hp
            client = cvm_client.CvmClient(cred,region,self.cp)
            req = models.DescribeInstanceTypeConfigsRequest()
            params = '{}'
            req.from_json_string(params)
            resp = client.DescribeInstanceTypeConfigs(req)
            return resp.to_json_string()
        except TencentCloudSDKException as e:
            return None
    #查看实例列表
    def get_describeinstances(self,region):
        try:
            cred = self.get_cred()
            self.hp.endpoint = "cvm.tencentcloudapi.com"
            self.cp.httpProfile = self.hp
            client = cvm_client.CvmClient(cred,region,self.cp)
            req = models.DescribeInstancesRequest()
            params = '{}'
            req.from_json_string(params)
            resp = client.DescribeInstances(req)
            return resp.to_json_string()
        except TencentCloudSDKException as e:
            return None

