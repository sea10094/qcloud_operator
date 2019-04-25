# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'NewPassword', 'type': 'str', 'method': random_string, 'myargs': ''},
         {'name': 'Accounts', 'type': 'str', 'method': random_accounts, 'myargs': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'},
         {'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''}]


output = [{'name':'TemplateId', 'type': 'int'}]

