# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'GlobalPrivileges', 'type': 'str', 'method': get_random_global_privileges, 'myargs': ''},
         {'name': 'DatabasePrivileges', 'type': 'str', 'method': get_random_database_privileges, 'myargs': ''},
         {'name': 'Accounts', 'type': 'str', 'method': random_accounts, 'myargs': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'},
         {'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''}]


output = [{'name':'TemplateId', 'type': 'int'}]

