# -*- coding: utf8 -*-
from utils import * 
import sys
sys.path.append("module")
import os

yun_api = {}

files = os.listdir('module')
for i in files:
    name = i.split('.')[0]
    yun_api[name] = __import__(name)     
    

def get_from_action(args):
    pass

def init():

  required_dict = {}

  required_dict['CreateParamTemplate'] = [{'name':'Name', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': ''}, 
                                        {'name':'Description', 'type': 'str', 'required': 'no', 'method': random_string, 'args': ''},
                                        {'name':'EngineVersion', 'type':'str', 'required': 'yes', 'method': random_choice, 'args': ['5.1', '5.5', '5.6', '5.7']}
                                       ]

  required_dict['DeleteParamTemplate'] = [{'name':'TemplateId', 'type': 'int', 'required': 'yes', 'method': get_from_action, 'args': ''}]
  required_dict['DescribeDefaultParams'] = [{'name':'EngineVersion', 'type': 'str', 'required': 'yes', 'method': random_choice, 'args': ['5.1', '5.5', '5.6', '5.7']}]
  required_dict['DescribeInstanceParamRecords'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeInstanceParams'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'aargs':''}]
  required_dict['DescribeParamTemplateInfo'] = [{'name':'TemplateId', 'type': 'int', 'required': 'yes', 'method': get_from_action, 'args': ''}]
  required_dict['DescribeParamTemplates'] = []
  required_dict['DescribeRollbackRangeTime'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['StartBatchRollback'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['CreateBackup'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                   {'name':'BackupMethod', 'type': 'str', 'required': 'yes', 'method': random_choice, 'args': ['logical', 'physical']}
                                  ]
  required_dict['DeleteBackup'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                   {'name':'BackupMethod', 'type': 'str', 'required': 'yes', 'method': random_choice, 'args': ['logical', 'physical']}
                                  ]
  required_dict['DescribeBackupConfig'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeBackupDatabases'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                              {'name':'StartTime', 'type': 'time', 'required': 'yes', 'method': get_random_time, 'args':''}
                                              #{'name':'SearchDatabase','type':'str', 'required':'no', 'method': random_string, 'args':''}
                                             ]
  required_dict['DescribeBackupTables'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                           {'name':'StartTime', 'type': 'time', 'required': 'yes', 'method': get_random_time, 'args':''},
                                           {'name':'DatabaseName', 'type': 'str', 'required': 'yes', 'method': get_from_action, 'args':''}
                                          ]
  required_dict['DescribeBackups'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeBinlogs'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeSlowLogs'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['ModifyBackupConfig'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                         {'name':'BackupMethod', 'type': 'str', 'required': 'yes', 'method': random_choice, 'args': ['logical', 'physical']}
                                        ]
  required_dict['AssociateSecurityGroups'] = [{'name':'SecurityGroupId', 'type': 'str', 'required': 'yes', 'method': get_sg_id, 'args':''},
                                              {'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}
                                             ]
  required_dict['DescribeDBSecurityGroups'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeProjectSecurityGroups'] = [{'name':'ProjectId', 'type':'int', 'required': 'yes', 'method': get_from_action, 'args':''}]
  required_dict['DisassociateSecurityGroups'] = [{'name':'SecurityGroupId', 'type': 'str', 'required': 'yes', 'method': get_sg_id, 'args':''},
                                              {'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}
                                             ]
  required_dict['ModifyDBInstanceSecurityGroups'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                                     {'name':'SecurityGroupIds', 'type':'str_array', 'required':'yes', 'method': get_sg_ids, 'args':''}
                                                    ]
  required_dict['CloseWanService'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeDBInstanceCharset'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeDBInstanceConfig'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeDBInstanceRebootTime'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeDBInstances'] = []
  required_dict['DescribeDBSwitchRecords'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeTagsOfInstanceIds'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['ModifyDBInstanceProject'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['ModifyDBInstanceVipVport'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                               {'name':'DstPort', 'type': 'int', 'required': 'yes', 'method': random_int, 'args': [1024, 65535]}
                                              ]
  required_dict['ModifyInstanceTag'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                         {'name':'ReplaceTags.', 'type': 'array of tag info', 'required': 'yes', 'method': random_tags, 'args':''}
                                        ]
  required_dict['OpenWanService'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['RestartDBInstances'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  
  required_dict['DescribeDatabases'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeTables'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                     {'name':'Database', 'type': 'str', 'required': 'yes', 'method': get_from_action, 'args':''}
                                    ] 
  required_dict['CreateAccounts'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'Accounts.', 'type': 'array of account', 'required': 'yes', 'method': random_string, 'args': ''},
                                      {'name':'Password', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': ''}
                                     ]
  required_dict['DeleteAccounts'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'Accounts.', 'type': 'array of account', 'required': 'yes', 'method': random_string, 'args': ''}
                                    ]
  required_dict['DescribeAccountPrivileges'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'User', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': ''},
                                      {'name':'Host', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': '%'}
                                    ]
  required_dict['DescribeAccounts'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['DescribeSupportedPrivileges'] =  [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''}]
  required_dict['ModifyAccountDescription'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'Accounts.', 'type': 'array of account', 'required': 'yes', 'method': random_string, 'args': ''},
                                      {'name':'Description', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': ''}
                                     ]
  required_dict['ModifyAccountPassword'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'Accounts.', 'type': 'array of account', 'required': 'yes', 'method': random_string, 'args': ''},
                                      {'name':'NewPassword', 'type': 'str', 'required': 'yes', 'method': random_string, 'args': ''}
                                     ]
  
  required_dict['ModifyAccountPrivileges'] = [{'name':'InstanceId', 'type': 'str', 'required': 'yes', 'method': get_instance_id, 'args':''},
                                      {'name':'Accounts.', 'type': 'array of account', 'required': 'yes', 'method': random_string, 'args': ''},
                                      {'name':'GlobalPrivileges.', 'type': 'str', 'required': 'yes', 'method': get_from_action, 'args': ''}
                                     ]
                                         
 
  output_dict = {}
  output_dict['CreateParamTemplate'] = [{'name':'TemplateId', 'type': 'int'}]
  output_dict['DescribeParamTemplates'] = [{'name':'TemplateId', 'type': 'int'}]


def ExecuteChoice(choice):
    pass
    
  

def MakeChoice():
    choice = random.sample(yun_api.keys(), 1)
    print choice
    yun_api[choice[0]].fun()



if __name__ == '__main__':
   init()
   MakeChoice()


