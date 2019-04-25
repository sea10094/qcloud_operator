# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''},
         {'name': 'SecurityGroupIds', 'type': 'array of string', 'method': random_sg_ids, 'myargs': ''}]



