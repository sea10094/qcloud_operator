# -*- coding: utf8 -*-


def flatten_request(obj):
    '''将Python基本类型（包括Dict、Array）的结构扁平化以满足云API的参数要求

    例如::
        {
            "InstanceSet": [
                {
                    "instanceId": "ins-xxx",
                    "sgIds": ["sg-xx", "sg-yy"]
                }
            ]
        }

        -->

        {
            "InstanceSet.0.instanceId": "ins-xxx",
            "InstanceSet.0.sgId.0": "sg-xx",
            "InstanceSet.0.sgId.1": "sg-yy",
        }
    '''
    result = {}
    if isinstance(obj, dict):
        for k in obj:
            _flatten_obj(obj[k], k, result)
    elif isinstance(obj, list):
        for idx, it in enumerate(obj):
            _flatten_obj(it, '%s' % idx, result)
    else:  # basic type
        result = obj
    return result

def _flatten_obj(obj, prefix, result):
    if isinstance(obj, dict):
        for k in obj:
            _flatten_obj(obj[k], prefix + '.%s' % k, result)
    elif isinstance(obj, list):
        for idx, it in enumerate(obj):
            _flatten_obj(it, prefix + '.%s' % idx, result)
    else:  # basic type
        result[prefix] = obj
