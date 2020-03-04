# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pro数据接口 
Created on 2017/07/01
@author: polo,Jimmy
@group : tushare.pro
"""

import pandas as pd
import simplejson as json
from functools import partial
import requests


class DataApi:

    __token = ''
    __http_url = 'http://api.tushare.pro'

    def __init__(self, token, timeout=10):
        """
        Parameters
        ----------
        token: str
            API接口TOKEN，用于用户认证
        """
        self.__token = token
        self.__timeout = timeout

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self.__http_url, json=req_params, timeout=self.__timeout)
        result = json.loads(res.text)
        if result['code'] != 0:
            raise Exception(result['msg'])
        data = result['data']
        columns = data['fields']
        items = data['items']

        return pd.DataFrame(items, columns=columns)

    def __getattr__(self, name):
        return partial(self.query, name)
