# -*- coding: utf-8 -*-

# @Time    : 2019/10/21
# @Author  : Lattine

# ======================
import requests
import hmac
import hashlib
import base64
import time
import random

appid = ''
bucket = ""
secret_id = ''  # 参考官方文档
secret_key = ''  # 同上

expired = time.time() + 2592000
onceExpired = 0
current = time.time()
rdm = ''.join(random.choice("0123456789") for i in range(10))
info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(rdm) + "&u=0&f="
print(info)
signature = bytes(info, encoding='utf-8')
secretkey = bytes(secret_key, encoding='utf-8')
my_sign = hmac.new(secretkey, signature, hashlib.sha1).digest()
bb = my_sign + signature
sign1 = base64.b64encode(bb)
sign2 = str(sign1, 'utf-8')
print(sign2)
url = "http://recognition.image.myqcloud.com/ocr/general"
headers = {'Host': 'recognition.image.myqcloud.com',
           "Authorization": sign2,
           }
files = {'appid': (None, appid),
         'bucket': (None, bucket),
         'image': ('1.jpg', open('d:/temp/0001.png', 'rb'), 'image/jpeg')
         }

r = requests.post(url, files=files, headers=headers)
responseinfo = r.content

print(responseinfo)
