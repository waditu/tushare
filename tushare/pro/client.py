# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pro数据接口 
Created on 2017/07/01
@author: polo
@group : tushare.pro
"""

import zmq
import pandas as pd
import simplejson as json
from functools import partial
from msgpack import unpackb, packb
from decimal import Decimal
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


class DataApi:

    __token = ''
    __http_url = 'http://api.tushare.pro'
    __tcp_url = 'tcp://tushare.pro:8003'

    def __init__(self, token, protocol='http'):
        """
        Parameters
        ----------
        protocol: str
            接口连接协议，支持http和tcp两种方式
        token: str
            API接口TOKEN，用于用户认证
        """
        self.__token = token
        self.__protocol = protocol

    def req_zmq_api(self, req_params):
        context = zmq.Context()

        socket = context.socket(zmq.REQ)
        socket.connect(self.__tcp_url)

        def hook(obj):
            if '__decimal__' in obj:
                obj = Decimal(obj['as_str'])
            return obj

        socket.send(packb(req_params, use_bin_type=True))

        raw_body = socket.recv()
        socket.close()
        
        result = unpackb(raw_body, object_hook=hook, raw=False)

        if result['code'] != 0:
            raise Exception(result['msg'])

        return result['data']

    def req_http_api(self, req_params):
        req = Request(
            self.__http_url,
            json.dumps(req_params).encode('utf-8'),
#             method='POST'
        )

        res = urlopen(req)
        result = json.loads(res.read().decode('utf-8'))

        if result['code'] != 0:
            raise Exception(result['msg'])

        return result['data']

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        if self.__protocol == 'tcp':
            data = self.req_zmq_api(req_params)
        elif self.__protocol == 'http':
            data = self.req_http_api(req_params)
        else:
            raise Warning('{} is unsupported protocol'.format(self.__protocol))

        columns = data['fields']
        items = data['items']

        return pd.DataFrame(items, columns=columns)

    def __getattr__(self, name):
        return partial(self.query, name)
