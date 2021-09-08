# coding=utf-8
# -*- coding:utf-8 -*-
import urllib2
import urllib
import json

'''json格式字段值替换'''
def replace_value(json_data, target, replacement):
    for key in json_data.keys():
        if type(json_data[key]) is dict:
            replace_value(json_data[key], target, replacement)
        else:
            if key == target:
                json_data[key] = replacement


'''json.loads与json.dumps特殊说明'''
# request = urllib2.Request()
# response = urllib2.urlopen(request)
# response = response.read()
# json_dict = json.loads(response)    \\json.loads转换后的格式为均为单引号包裹，结果为：{'key': 'value'},格式默认带空格
# json_text = replace_value(json_text,target,replacement)    \\得到替换后的dict
# json_to_str = json.dumps(json_text,separators=(',',':'))   \\json.dumps()可转换成标准json格式字符串（双引号进行包裹），设置separators=(',',':')可以去掉格式中的空格。结果为：{"key":"value"}，无空格
