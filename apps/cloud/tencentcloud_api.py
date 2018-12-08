# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client,models
from omsbackend import settings
from utils import create_signature
import requests
import time
import sys
import random
import ssl
import base64
import hmac
import hashlib

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

    def get_project(self,region=''):
       try:
           mysignature = create_signature.create_signature(action='DescribeProject',region=region)
           url ='https://account.api.qcloud.com/v2/index.php'
           timestamp =int(time.time())
           nonce = random.randint(1, sys.maxsize)
           secret_key = self.secretkey.encode(encoding='utf-8')
           srcStr = "GETaccount.api.qcloud.com/v2/index.php?Action=DescribeProject&Nonce=%s&Region=%s&SecretId=%s&Signature=%s&Timestamp=%s&Version=2017-08-09" %(nonce,region,self.secretid,mysignature,timestamp)
           srcStr = srcStr.encode(encoding='utf-8')
           digest = hmac.new(secret_key,srcStr,digestmod=hashlib.sha1).digest()
           digest_b64 = base64.b64encode(digest)
           signStr = digest_b64.decode(encoding='utf-8')
           params = {
               'Action':'DescribeProject',
               'SecretId' :self.secretid,
               'Region':region,
               'Timestamp':timestamp,
               'Nonce':nonce,
               'Signature':signStr,
           }
           response = requests.get(url,params=params)
           print(response.json())
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

