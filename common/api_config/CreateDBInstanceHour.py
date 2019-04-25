# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *


input = [{'name': 'GoodsNum', 'type': 'int', 'method': constant_int, 'myargs': '1'},
         {'name': 'Memory', 'type': 'int', 'method': constant_int, 'myargs': '8000'},
         {'name': 'Volume', 'type': 'int', 'method': constant_int, 'myargs': '200'},
         {'name': 'EngineVersion', 'type': 'str', 'method': random_choice, 'myargs': [ '5.6'], 'required': 'optional'},
         #{'name': ['UniqVpcId', 'UniqSubnetId'], 'type': 'str', 'method': random_vpc, 'myargs': ''},
         {'name': ['InstanceRole', 'MasterRegion', 'MasterInstanceId', 'Region'], 'type': 'str', 'method': random_mode, 'myargs': ['dr'], 'required': 'optional'},
         {'name': 'Port', 'type': 'str', 'method': random_int, 'myargs': [1024, 65535], 'required': 'optional'},
         {'name': 'ProtectMode', 'type': 'int', 'method': random_choice, 'myargs': [0, 1, 2], 'required': 'optional'},
         {'name': 'DeployMode', 'type': 'int', 'method': constant_int, 'myargs': '0', 'required': 'optional'},
         {'name': 'RoGroup', 'type': 'RoRroup', 'method': get_ro_group, 'myargs': '', 'required': 'optional'},
        ]


traversal = [{'name': 'GoodsNum', 'range': [1,2]},
             {'name': 'Memory', 'range': [8000]},
             {'name': 'Volume', 'range': [200]},
             {'name': 'EngineVersion', 'range': [ '5.6', '5.7', '5.5' ], 'required': 'optional'},
             {'name': 'MasterInstanceId', 'range': [ 'cdb-8yr3nkax' ], 'required': 'optional'},
             {'name': 'InstanceRole', 'range': [ 'master', 'ro', 'dr' ], 'required': 'optional'},
             {'name': 'MasterRegion', 'range': [ 'ap-guangzhou' ], 'required': 'optional'},
             {'name': 'Region', 'range': [ 'ap-guangzhou' , 'ap-shanghai', 'ap-beijing'], 'required': 'optional'},
             {'name': 'Port', 'range': [ 1025, 32673 ], 'required': 'optional'},
             {'name': 'Password', 'range': [ '12345678' , 'mada@chengdu', '#*>>>?'], 'required': 'optional'},
             {'name': 'ProtectMode', 'range': [ 0, 1, 2], 'required': 'optional'},
             {'name': 'RoGroup', 'range': [ {'RoGroupMode': 'alone'} ,{'RoGroupMode': 'join'} , {'RoGroupMode': 'alinone'}], 'required': 'optional'},
            ]

           

