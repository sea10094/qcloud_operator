# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''},
         {'name': 'StartTime', 'type': 'str', 'method': constant_string, 'myargs': '2017-07-12 10:29:20'},
         {'name': 'DatabaseName', 'type': 'str', 'method': get_random_database, 'myargs': ''}]



