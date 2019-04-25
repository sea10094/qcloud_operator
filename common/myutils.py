# -*- coding: utf8 -*-
import random,string
import time
from datetime import datetime
import common_api


def random_string(req,resp):
    ret = 0
    if resp == '':
       ret = random.sample('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()',10)
    else:
       ret = random.sample(resp, 8)
    ret = ''.join(ret)
    return ret

def random_description(req,resp):
    return "motor test " + random_string('')

def random_choice(myreq,resp):
    if resp != '':
       ret = random.sample(resp, 1)[0]
    else:
       ret = ''
    return ret


def get_sg_ids(req,resp):
    pass

def get_sg_id(req,resp):
    pass

def strTimeProp(start, end, prop, frmt): 
    stime = time.mktime(time.strptime(start, frmt)) 
    etime = time.mktime(time.strptime(end, frmt)) 
    ptime = stime + prop * (etime - stime) 
    return int(ptime)

def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'): 
    return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))

def get_random_time(req,resp):
    start = '2018-06-02 12:12:12'
    end = '2018-11-01 00:00:00'
    return randomDate(start,end)

def random_int(req,resp):
    return random.randint(1024, 65535)

def random_tags(req,resp):
    pass

def random_accounts(myreq,resp):
    x = random.randint(1,5)
    accounts = []
    for i in range(x):
        user = random_string(myreq,resp)
        account = {'User': user, 'Host': '%'}
        accounts.append(account)
    return accounts

def get_instance_id(req,resp):
    #return 'cdb-ppzlefme'
    return 'cdb-mvtljhdk'

def get_instance_ids(last_req, last_resp):
    #return ['cdb-ppzlefme', "cdb-immgxo0o", 'cdb-824ajvcu']
    return ['cdb-mvtljhdk', "cdb-6437sm3a", 'cdb-nren3bss']

def random_exist_accounts(req,resp):
    ret = common_api.init()
    ret = common_api.execute_choice('DescribeAccounts')
    ret = ret['Response']['Items']
    myitem = ['User', 'Host']
    return_list = []
    for i in ret:
        retcode={key:value for key,value in i.items() if key in myitem}
        if retcode['Host'] != 'localhost':
           return_list.append(retcode)

    num = random.randint(1, len(return_list))
    to_delete = random.sample(return_list, num)
    return to_delete 

def random_exist_user(req,resp):
    ret = common_api.init()
    ret = common_api.execute_choice('DescribeAccounts')
    ret = ret['Response']['Items']
    myitem = ['User', 'Host']
    return_list = []
    for i in ret:
        retcode={key:value for key,value in i.items() if key in myitem}
        return_list.append(retcode)

    to_describe = random.sample(return_list, 1)
    return to_describe[0]['User'] 

def get_default_host(req,resp):
    return '%'   


def get_random_global_privileges(req,resp):
    common_api.init()
    supported_privileges = common_api.execute_choice('DescribeSupportedPrivileges')
    privilege_list = supported_privileges['Response']['GlobalSupportedPrivileges']
    num = len(privilege_list)
    random_privilege_list = random.sample(privilege_list, num)
    return random_privilege_list

def get_random_database_privileges(req,resp):
    common_api.init()
    supported_privileges = common_api.execute_choice('DescribeSupportedPrivileges')
    privilege_list = supported_privileges['Response']['DatabaseSupportedPrivileges']
    num = len(privilege_list)
    random_privilege_list = random.sample(privilege_list, num)
    ret = common_api.execute_choice('DescribeDatabases')
    databases = ret['Response']['Items']
    selected_database = random.sample(databases, 1)[0]
    return [{'Database': selected_database, 'Privileges': random_privilege_list}]

def get_random_database(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeDatabases')
    databases = ret['Response']['Items']
    selected_database = random.sample(databases, 1)[0]
    return selected_database
    
def random_exist_database(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeDatabases')
    databases = ret['Response']['Items']

    selected_database = random.sample(databases, 1)[0]
    return selected_database


def constant_string(req,resp):
    return req,resp

def constant_int(req,resp):
    return int(req,resp)

def random_rollback_time(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeBackups')
    answer = ret['Response']
    if answer['Items'] != []:
       selected_item = random.sample(answer['Items'], 1)[0]
       instance_id = get_instance_id('', '')
       start_time = selected_item['Date']
       return [instance_id, start_time]
    return ['', '']


    
def random_RollbackInstancesInfo(req,resp):
    instance_id = eval(resp[0])('', '')
    strategy = random_choice(req,resp[1])
    instance_id, start_time = random_rollback_time('', '')
    return [{'InstanceId': instance_id, 'Strategy': strategy, 'RollbackTime': start_time}]
    
def random_template_id(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeParamTemplates')
    items = ret['Response']['Items']
    if items != []:
       selected_item = random.sample(items, 1)[0]
       return selected_item['TemplateId']
       
    return 0

def random_parameters(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeInstanceParams')
    items = ret['Response']['Items'] 
    selected_items = random.sample(items, random.randint(1, len(items)))
    parameters = []
    for i in selected_items:
        if i['EnumValue'] != []:
           value = random.sample(i['EnumValue'], 1)[0]
           tmp = {'Name': i['Name'], 'CurrentValue': value}
           parameters.append(tmp)
        else:
           value = random.randint(i['Min'], i['Max'])
           tmp = {'Name': i['Name'], 'CurrentValue': value}
           parameters.append(tmp)

    return parameters
 
           
def random_sg_id(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeSecurityGroups', 'vpc', '2017-03-12')
    sg_groups = ret['Response']['SecurityGroupSet']
    sg_ids = []
    for i in sg_groups:
        sg_ids.append(i['SecurityGroupId'])
    selected_sg_ids = random.sample(sg_ids, 1)
    return selected_sg_ids[0]

def random_sg_ids(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeSecurityGroups', 'vpc', '2017-03-12')
    sg_groups = ret['Response']['SecurityGroupSet']
    sg_ids = []
    for i in sg_groups:
        sg_ids.append(i['SecurityGroupId'])
    selected_sg_ids = random.sample(sg_ids, random.randint(1, len(sg_ids)))
    return selected_sg_ids


def random_vpc_id(req,resp):
    common_api.init()
    ret = common_api.execute_choice('DescribeVpcs', 'vpc', '2017-03-12')
    vpc_set = ret['Response']['VpcSet']
    vpc_ids = []
    for vpc in vpc_set:
        vpc_ids.append(vpc['VpcId'])
    selected_vpc_id = random.sample(vpc_ids, 1)
    return selected_vpc_id

def random_vpc(req,resp):
    common_api.init()
    vpc_id = random_vpc_id('')
    vpc_id = 'vpc-jeck8wsr'
    subnet_id = ''
    ret = common_api.execute_choice('DescribeSubnets', 'vpc', '2017-03-12')
    subnet_set = ret['Response']['SubnetSet']
    for vpc in subnet_set:
        if vpc['VpcId'] == vpc_id:
           subnet_id = vpc['SubnetId']
    
    if subnet_id == '':
       return random_vpc(req,resp)
    return [vpc_id, subnet_id] 
    
def get_master_instance_id(req,resp):
    import ConfigParser
    import json
 
    conf = ConfigParser.ConfigParser()  

    conf.read("my.cfg")  

    master = json.loads(conf.get("test", "master"))
    if master == []:
       return get_instance_id('')
    else:
       return random.sample(master, 1)[0]

def get_region(master_id):
    common_api.init()
    ret = common_api.execute_choice('DescribeDBInstanceConfig')
    
    zone = ret['Response']['Zone'].split('-')[:-1]
    return zone
    
        
def random_mode(req,resp):
    mode = random_choice(req,resp)
    master_region = ''
    master_instance_id = ''
    if mode == 'master':
       pass
    elif mode == 'ro':
       master_instance_id = get_master_instance_id('')
    elif mode == 'dr': 
       master_instance_id = get_master_instance_id('')
       master_region = 'ap-guangzhou'

    if mode == 'dr':
       return [mode, master_region, master_instance_id, 'ap-beijing']
    else:
       return [mode, master_region, master_instance_id, 'ap-guangzhou']
       

def random_subnet_id(req,resp):
    pass


def random_zone(req,resp):
    pass


def get_ro_group(req,resp):
    return {'RoGroupMode': 'alone'}


def delete_db_instances(instance_ids):
    import time
    time.sleep(30)
    common_api.init()
    for instance_id in instance_ids:
        ret = common_api.execute_choice2('IsolateDBInstance', instance_id)
    

def get_last_instance_ids(req, resp):
    if resp.has_key('InstanceIds'):
       return resp['InstanceIds']
    else:
       return []

def get_last_instance_id(last_req, last_resp):
    if last_resp['Items'] != []:
       return last_resp['Items'][0]['InstanceId']
    else:
       return -1

def get_param_value(req_list, resp_list, index, param):
    current_resp = resp_list[index]
    
    if current_resp.has_key(param):
          return current_resp[param]
    return ''

def get_param_dict(req_list, resp_list, index, params):
    current_resp = resp_list[index]
    ret_dict = {} 
    for key in params:
       if current_resp.has_key(key):
          ret_dict[key] = current_resp[key]
    return ret_dict

def get_secret_from_last_resp(last_req, last_resp):
    ret_dict = {}
    if last_resp.has_key('secretId'):
       ret_dict['s_id'] = last_resp['secretId']
    if last_resp.has_key('secretKey'):
       ret_dict['s_key'] = last_resp['secretKey']
    if last_resp.has_key('uin'):
       ret_dict['sub_uin'] = last_resp['uin']
    return ret_dict

def get_uin_from_last_resp(last_req, last_resp):
    ret_dict = {}
    if last_resp.has_key('uin'):
       return last_resp['uin']
    return ''


def relax():
    import time
    time.sleep(120)

def get_instance_id_from_req(last_req, last_resp):
    return last_req['InstanceId']


def get_rollback_time_from_resp(last_req, last_resp):
    for i in last_resp['Items']:
       if i['Status'] == 'SUCCESS': 
          return i['Date']

def get_dict_from_dict_list(mydict, kv):    
    mylist = kv[0]
    index = kv[1]
    return mydict[mylist][index] 

def get_random_paramlist(req_list, rsp_list, index, params):
    param_list = rsp_list[index]['Items']
    selected_param = random.sample(param_list, 1)[0]
    slct_value = ''
    if selected_param['EnumValue'] != []:
       slct_value = random.sample(selected_param['EnumValue'], 1)[0]
    else:
       slct_value = random.randint(selected_param['Min'], selected_param['Max'])
    return [{'Name': selected_param['Name'], 'CurrentValue': slct_value}]

def get_ins_info_by_kv(req_list, rsp_list, index, params):
    instances = rsp_list[index]
    mylist = params.split('&')
    dst_key = mylist[0]
    src_key = mylist[1]
    src_value = mylist[2]
    for i in instances['Items']:
        try:
          if str(i[src_key]) == src_value:
             return i[dst_key]
        except:
          pass
    return 'null'


def get_paramlist_value(req_list, rsp_list, index, params):
    param = req_list[index]['ParamList'][0]
    return param[params]




def get_dict_from_list(mylist, kv):
    key = kv[0]
    value = kv[1]
    for mydict in mylist:
        if mydict[key] == value:
           return mydict  
    return {}


def get_dict(originlist, params):
    
    mylist = []
    kv = params[1]
    list_filter = params[0]
    key = kv[0]
    value = kv[1]
    for i in list_filter:
        mylist = originlist[i]
        
    for mydict in mylist:
        if type(mydict) == type({}) and mydict[key] == value:
           return mydict  
    return {}
