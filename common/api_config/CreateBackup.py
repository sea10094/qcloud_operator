# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'InstanceId', 'type': 'str', 'method': get_instance_id, 'myargs': ''},
         {'name': 'BackupMethod', 'type': 'str', 'method': random_choice, 'myargs': ['logical', 'physical']}]



