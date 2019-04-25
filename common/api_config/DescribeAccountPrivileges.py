# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'User', 'type': 'str', 'method': random_exist_user, 'myargs': ''},
         {'name': 'Host', 'type': 'str', 'method': get_default_host, 'myargs': ''},
         {'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''}]



