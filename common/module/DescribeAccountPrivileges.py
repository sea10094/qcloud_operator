# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests

secret_id = "AKIDt1tcCFhao9bgiwCN0JFHQpQC4ndbYjcy"
secret_key = "G308aAqcWaqREGW926ICTrMJQf14NeDI"

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)

def fun(instance_id, user1, host1):
    endpoint = "cdb.tencentcloudapi.com"
    mytime = int(time.time())
    data = {
        'Action' : 'DescribeAccountPrivileges',
        'Nonce' : 11886,
        'Region' : 'ap-guangzhou',
        'SecretId' : secret_id,
        'Timestamp' : mytime, # int(time.time())
        'Version': '2017-03-20',
        'InstanceId': instance_id,
        'User': user1,
        'Host': host1,
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    # 此处会实际调用，成功后可能产生计费
    resp = requests.get("https://" + endpoint, params=data)
    # print(resp.url)
    return resp.json()

if __name__ == '__main__':
   fun()
