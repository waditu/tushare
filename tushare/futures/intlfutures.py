# -*- coding:utf-8 -*-

"""
国际期货
Created on 2016/10/01
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import json
import six
import pandas as pd
from tushare.futures import cons as ct

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
    
    
def get_intlfuture(symbols=None):
    symbols = ct.INTL_FUTURE_CODE if symbols is None else symbols
    df = _get_data(ct.INTL_FUTURE_URL%(ct.P_TYPE['http'], ct.DOMAINS['EM'], 
                   ct.PAGES['INTL_FUT'], symbols,
                   _random(17)))
    print(df)
  
def _get_data(url):
    try:
        request = Request(url)
        data_str = urlopen(request, timeout=10).read()
#         data_str = data_str.decode('GBK')
        data_str = data_str.split('=')[1]
#         data_str = """
#         {futures:["CONX0,CONX,美原油11,50.32,50.23,49.80,50.58,49.72,0,137713,0.00,0,0,50.32,0.00,0,181562,-0.52,-1.03%,0.00,831,137713,0,-1,1,0.00,0.00,2016-10-17 21:38:49,0","GLNZ0,GLNZ,美黄金12,1251.7,1252.6,1256.9,1258.0,1251.1,0,67082,0.0,0,0,1251.7,0.0,0,373385,5.2,0.42%,0.0,62,67082,0,-1,0,0.0,0.0,2016-10-17 21:38:41,0"]}
#         """
        data_str = data_str.replace('futures', '"futures"')
        if six.PY3:
            data_str = data_str.decode('utf-8')
        data_str = json.loads(data_str)
        df = pd.DataFrame([[col for col in row.split(',')] for row in data_str.values()[0]]
                        )
        df = df[[1, 2, 5, 4, 6, 7, 13, 9, 17, 18, 16, 21, 22]]
        df.columns = ct.INTL_FUTURES_COL
        return df
    except Exception as er:
        print(str(er))  
        
        
def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

