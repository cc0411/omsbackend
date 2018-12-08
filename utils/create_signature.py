# -*- coding: utf-8 -*-
import base64
import binascii
import hashlib
import hmac
import random
import sys
import time
from omsbackend.settings import SECRETKEY,SECRETID
def  create_signature(action,region=''):
    # 设置参数
    param = {}
    # 公共参数
    # Nonce最好是随机数
    param["Nonce"] = random.randint(1, sys.maxsize)
    # Timestamp最好是当前时间戳
    param["Timestamp"] = int(time.time())
    param["SecretId"] = SECRETID
    param["Version"] = "2018-07-09"
    param["Region"] = region
    param["Action"] = action
    # 生成待签名字符串
    sign_str = "GETaccount.api.qcloud.com/?"
    sign_str += "&".join("%s=%s" % (k, param[k]) for k in sorted(param))

    # 生成签名
    secret_key = SECRETKEY
    if sys.version_info[0] > 2:
        sign_str = bytes(sign_str, "utf-8")
        secret_key = bytes(secret_key, "utf-8")
    hashed = hmac.new(secret_key, sign_str, hashlib.sha1)
    signature = binascii.b2a_base64(hashed.digest())[:-1]
    if sys.version_info[0] > 2:
        signature = signature.decode()
    print(signature)

    return signature
