#!/usr/bin/env python
# -*- coding:utf-8 -*- 

'''
Created on 2016年9月1日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
'''

import datetime
import json
import uuid
import time
import six

def nowtime_str():
    return time.time() * 1000


def get_jdata(txtdata):
    txtdata = txtdata.content
    if six.PY3:
        txtdata = txtdata.decode('utf-8')
    jsonobj = json.loads(txtdata)
    return jsonobj
        

def json_load(path):
    with open(path) as f:
        return json.load(f)
    
    
def str2num(num_str, convert_type='float'):
    num = float(grep_comma(num_str))
    return num if convert_type == 'float' else int(num)


def grep_comma(num_str):
    return num_str.replace(',', '')


def get_mac():
    return ("".join(c + "-" if i % 2 else c for i, c in enumerate(hex(
        uuid.getnode())[2:].zfill(12)))[:-1]).upper()
        

if __name__ == '__main__':
    print(json_load('D:\\waditu\\workspace\\tushare\\tushare\\trader\\csc.json'))