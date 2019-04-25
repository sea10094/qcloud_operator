# -*- coding: utf8 -*-
import sys
sys.path.append('../')
from  myutils import *
import secret

tmp = {'version':'2.0','statement':[{'action':'cdb:*','effect':'allow','resource':'qcs::vpc:gz::*/*'}]}
import json

actions = [
           {'mytype': 'front', 'postpath': '/interface.php', 'myproduct': 'test.mcproxy.tencentyun.com', "version":1,"componentName":"MC_CDB",'spanId': '', "eventId":1341125155,"seqId":"35b42f88-7874-ce33-53cb-1690fd2c7958","interface":{"interfaceName":"active.ptlogin.setLoginFlag","para":{"uin":secret.uin,"skey":secret.skey}}},
           {'mytype': 'front', 'postpath': '/interface.php', 'myproduct': 'test.mcproxy.tencentyun.com', "version":1,"componentName":"MC_CDB","eventId":1341125155,"seqId":"35b42f88-7874-ce33-53cb-1690fd2c7958","spanId":"","interface":{"interfaceName":"active.ptlogin.verify","para":{"uin":secret.uin,"skey":secret.skey, "domain_id":0,"need_nick":1}}},
           {'myproduct': 'cdb.cloud.tencent.com', "offset":0,"limit":50,"withDr":2,"withExCluster":1,"status":[0,1,4],"instanceTypes":[1,2,3,4],'mc_gtk': str(secret.csrfCode), 'mytype': 'front', 'regionId': 1, 'postpath': '/api/server-cgw/cdb/qcloud.Qcdb.v3.DescribeDBInstances'},
           ]
