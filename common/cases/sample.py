# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  common.myutils import *
import common.secret

tmp = {'version':'2.0','statement':[{'action':'*','effect':'allow','resource':'qcs::cdb:ap-guangzhou:uin/100000007940:instance/cdb-hu9zf08o'}]}
import json

actions = [
           {'Action': 'DescribeProject', 'myproduct': 'account', 'mytype': 'v2', 'projectName': 'cdb_account', 'post_resp': [get_dict_from_list, ['projectName', 'resource-pool1']]},
           {'Action': 'DescribeProject', 'myproduct': 'account', 'mytype': 'v2', 'projectName': 'cdb_account', 'post_resp': [get_dict_from_list, ['projectName', 'resource-pool2']]},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Limit': 1, 'Status': [1], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [0], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [4], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [5], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [0], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [1], 'ProjectId': {'transfer_function': get_param_value, 'index': 1, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [1], 'ProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}, 'InstanceTypes': [1], 'EngineVersions': ['5.7'], 'post_resp': [get_dict, [['Items'], ['EngineVersion', '5.7']]]},
           {'Action':'ModifyDBInstanceProject', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'InstanceIds': [{'transfer_function': get_param_value, 'index': 8, 'params': 'InstanceId'}], 'NewProjectId': {'transfer_function': get_param_value, 'index': 1, 'params': 'projectId'}},
           {'Action':'DescribeDBInstances', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'Status': [1], 'ProjectId': {'transfer_function': get_param_value, 'index': 1, 'params': 'projectId'}},
           {'Action':'ModifyDBInstanceProject', 'myproduct': 'cdb', 'mytype': 'v3', 'Region': 'ap-nanjing', 'InstanceIds': [{'transfer_function': get_param_value, 'index': 8, 'params': 'InstanceId'}], 'NewProjectId': {'transfer_function': get_param_value, 'index': 0, 'params': 'projectId'}},
           ]
