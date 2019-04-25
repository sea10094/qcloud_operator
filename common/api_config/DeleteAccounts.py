# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'Accounts', 'type': 'str', 'method': random_exist_accounts, 'myargs': ''},
         {'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''}]


output = [{'name':'TemplateId', 'type': 'int'}]

