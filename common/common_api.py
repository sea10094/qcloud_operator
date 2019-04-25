# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests

import sys
import random
import flatten_request
from urllib import quote

sys.path.append('cases')
#sys.path.append('api_config')
import os

import secret
import uuid
from product_info import products

secret_id = secret.secret_id
secret_key = secret.secret_key

api_configs = {}
cgw_headers = {'X-QCloud-User-ID': '3227991405', 'X-QCloud-Component-ID': 'qctestsite', 'X-QCloud-Transaction-ID': 'ee222292-4058-49ac-880a-4d3da951c1f7'}

def init():
    global api_configs
    files = os.listdir('cases')
    for i in files:
       name = i.split('.')[0]
       api_configs[name] = __import__(name)     
    #files = os.listdir('api_config')
    #for i in files:
    #   name = i.split('.')[0]
    #   api_configs[name] = __import__(name)     

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)


def get_signature(end, param, s_key):
    request_host = end + ".api.qcloud.com"
    request_uri = '/v2/index.php'

    keys = sorted(param.keys())
    queryStr = []
    for key in keys:
        queryStr.append("%s" % (key + "=" + str(param[key])))
    sourceStr = "GET" + request_host + request_uri + "?" + "&".join(queryStr)

    hashed = hmac.new(s_key, sourceStr, hashlib.sha256)
    x = base64.b64encode(hashed.digest())[:-1]
    return quote(x)

def fun4front(args, end = 'cdb', region = 'ap-nanjing'):

    postpath = args['postpath']
    args.pop('postpath')
    endpoint = end 


    mytime = int(time.time())
    common = {
    }

    headers = {}
    headers['Cookie'] = secret.cookie
    headers['X-CSRF-Token'] = str(secret.csrfCode)

    data = dict(common.items() + args.items())
    # 此处会实际调用，成功后可能产生计费
    resp = requests.post("http://" + endpoint + postpath, json=data, headers = headers, verify=False)
    import json
    log = json.dumps(data) + '%' + resp.content.decode('unicode-escape').encode('utf-8')
    print log
    #print resp.content.decode('unicode-escape').encode('utf-8')
    #print resp.content
    return resp.json()


def fun4cgw(args, uin = secret.uin, end = 'cdb', version = '2017-03-20', region = 'ap-nanjing'):

    postpath = "/interfaces/interface.php"
    endpoint = "nj.cdb.cgateway.tencentyun.com"

    mytime = int(time.time())
    common = {
        'RequestId': str(uuid.uuid1()),
        'AppId': secret.app_id,
        'Uin':secret.uin,
        'SubAccountUin': uin,
        "ClientIp":"139.198.188.222",
        "ApiModule":"cdb",
        "RequestSource":"API",
        'Version': version,
    }
    data = dict(common.items() + args.items())
    # 此处会实际调用，成功后可能产生计费
    resp = requests.post("http://" + endpoint + postpath, headers = cgw_headers, json=data, verify=False)
    #resp = requests.post("http://" + endpoint + postpath,  json=data, verify=False)
    import json
    log = json.dumps(data) + '%' + resp.content.decode('unicode-escape').encode('utf-8')
    print log
    #print resp.content.decode('unicode-escape').encode('utf-8')
    #print resp.content
    return resp.json()

def funv2(args, secret_id, s_key, end, region):

    endpoint = end + '.api.qcloud.com'
    url = '/v2/index.php'
    mytime = int(time.time())
    common = {
        'Nonce' : 11886,
        'Region' : region,
        'SecretId' : secret_id,
        'Timestamp' : mytime, # int(time.time())
        'SignatureMethod':'HmacSHA256',
    }
    if args.has_key('Region'):
       common.pop('Region')
    data = dict(common.items() + args.items())
    data["Signature"] = get_signature(end, data, s_key)
    resp = requests.get("https://" + endpoint + url, params=data, verify=False)
    # print(resp.url)
    import json
    log = json.dumps(data) + '%' + resp.content.decode('unicode-escape').encode('utf-8')
    print log
    #print resp.content.decode('unicode-escape').encode('utf-8')
    #print resp.content
    ret = resp.json()
    if ret['code'] != 0:
       time.sleep(1)
       ret = funv2(args, secret_id, s_key, end, region)
    return ret


def funv3(args, secret_id, s_key, end, version, region):

    endpoint = end + ".tencentcloudapi.com"
    mytime = int(time.time())
    common = {
        'Nonce' : 11886,
        'Region' : region,
        'SecretId' : secret_id,
        'Timestamp' : mytime, # int(time.time())
        'Version': version,
    }
    if args.has_key('Region'):
       common.pop('Region')
    data = dict(common.items() + args.items())
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(s_key, s, hashlib.sha1)
    # 此处会实际调用，成功后可能产生计费
    resp = requests.get("https://" + endpoint, params=data, verify=False)
    # print(resp.url)
    import json
    log = json.dumps(data) + '%' + resp.content.decode('unicode-escape').encode('utf-8')
    print log
    #print resp.content.decode('unicode-escape').encode('utf-8')
    #print resp.content
    return resp.json()

def random_args(choice):
   interface = {'Action': choice}
   args = {}
   if not api_configs.has_key(choice):
      return args

   for i in api_configs[choice].input:
       if i.has_key('required') and i['required'] == 'optional':
             continue

       if type(i['name']) == type(''):
          value = i['method']('', i['myargs'])
          tmp = {i['name']:value}
          args = dict(tmp.items() + args.items())
       elif type(i['name']) == type([]):
          values = i['method'](i['myargs'])
          for j in range(len(i['name'])):
              tmp = {i['name'][j]:values[j]}
              args = dict(tmp.items() + args.items())

   return args

def instead_of_param(action, req_list, resp_list):
           if type(action) == type({}) and action.has_key('transfer_function'):
              index = action['index']
              params = action['params']
              action = action['transfer_function'](req_list, resp_list, index, params)
              #return action
           elif type(action) == type([]):
              for i in action[:]:
                  ret = instead_of_param(i, req_list, resp_list)
                  action.remove(i)
                  action.append(ret)
                  
           elif type(action) == type({}):
              for key in action.keys():
                  ret = instead_of_param(action[key], req_list, resp_list)
                  if ret != -1:
                     action[key] = ret

           return action



def do_action(action, req_list, resp_list, end, version, itf_type):


       s_id = secret.secret_id
       s_key = secret.secret_key
       uin = secret.uin

       if action.has_key('use_child_account'):
          s_id = secret.sub_secret_id
          s_key = secret.sub_secret_key
          uin = secret.sub_uin
          action.pop('use_child_account')

             

       if itf_type == 'v3':
          ret = funv3(flatten_request.flatten_request(action), s_id, s_key, end, version, 'ap-nanjing')
       elif itf_type == 'v2':
          ret = funv2(flatten_request.flatten_request(action), s_id, s_key, end, 'nj')
       elif itf_type == 'cgw':
          ret = fun4cgw(action, uin)
       elif itf_type == 'front':
          ret = fun4front(action,end)
          

       if ret.has_key('Response'):
          return  [action, ret['Response']]
       if ret.has_key('data'):
          return  [action, ret['data']]
       return ['', '']
              

def validate_kv(rsp, k, v):
    param_list = rsp['Items']
    
    for param in param_list:
        
        if param['Name'] == k: 
           if param['CurrentValue'] == v:
            print '%s %s validate ok'  %(param['Name'],param['CurrentValue']) 
            return 0
    
    print '%s %s validate error'  %(param['Name'],param['CurrentValue']) 
    

def do_choice(choice, end = 'cdb', version = '2017-03-20'):
   last_req = {}
   last_resp = {}
   resp_list = []
   req_list = []
   for action in api_configs[choice].actions:
       instead_of_param(action, req_list, resp_list)
       post_resp = ''
       validate_params = ''
       product = action['myproduct']
       action.pop('myproduct')

       itf_type = action['mytype']
       action.pop('mytype')

       if action.has_key('post_resp'):
          post_resp = action['post_resp']
          action.pop('post_resp')

       if action.has_key('validate_kv'):
          validate_params = action['validate_kv']
          action.pop('validate_kv')

       if products.has_key(product):
          [last_req, last_resp] = do_action(action, req_list, resp_list, product, products[product], itf_type)
       else:
          [last_req, last_resp] = do_action(action, req_list, resp_list, product, '', itf_type)

       if post_resp != '':
          last_resp = post_resp[0](last_resp, post_resp[1])

       if validate_params != '':
          validate_kv(last_resp, validate_params[0], validate_params[1])

       resp_list.append(last_resp)
       req_list.append(last_req)


       if type(last_resp) == type({}) and last_resp.has_key('AsyncRequestId'):
          itf = {'Action': 'DescribeAsyncRequestInfo'}
          args = {'AsyncRequestId': last_resp['AsyncRequestId']}
          args = dict(args.items() + itf.items())
      
          status = 0
          while status == 0:
            ret = fun4cgw(args)['Response']
            if ret['Status'] == 'FAILED' or ret['Status'] == 'SUCCESS':
               status = 1
           



def execute_choice(choice, end = 'cdb', version = '2017-03-20'):
   interface = {'Action': choice}
   args = {}
   for i in api_configs[choice].input:
       if i.has_key('required') and i['required'] == 'optional':
             continue

       if type(i['name']) == type(''):
          value = i['method']('', i['myargs'])
          tmp = {i['name']:value}
          args = dict(tmp.items() + args.items())
       elif type(i['name']) == type([]):
          values = i['method'](i['myargs'])
          for j in range(len(i['name'])):
              tmp = {i['name'][j]:values[j]}
              args = dict(tmp.items() + args.items())
   
   if 'end' in dir(api_configs[choice]):
      end = api_configs[choice].end
      version = api_configs[choice].version
      ret = fun4cgw(interface, args, end, version)
   else:
      ret = fun4cgw(interface, args)

   if ret['Response'].has_key('AsyncRequestId'):
      itf = {'Action': 'DescribeAsyncRequestInfo'}
      args = {'AsyncRequestId': ret['Response']['AsyncRequestId']}
      
      status = 0
      while status == 0:
            ret = fun2(itf, args)
            if ret['Response']['Status'] == 'FAILED' or ret['Response']['Status'] == 'SUCCESS':
               status = 1
   else:
      return ret

def todo(choice):
    init()
    do_choice(choice)

if __name__ == '__main__':
   #interface = {'Action': 'DescribeDBInstances'}
   #args = {}
   #fun(interface, args)
   #interface = {'Action': 'CreateAccounts'}
   #args = {'Accounts': [{'User':'mada2', 'Host':'%'}], 'Password':'mada@20140306'}
   #fun(interface, args)
   init()
   if len(sys.argv) == 2:
      choice = sys.argv[1]
   else:
      choice = random.sample(api_configs.keys(), 1)[0]
   do_choice(choice)

