# -*- coding:utf-8 -*- 
"""
通联数据
Created on 2015/08/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

from pandas.compat import StringIO
import pandas as pd
from tushare.util import vars as vs
from tushare.util.common import Client
from tushare.util import upass as up

class Idx():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def Idx(self, secID='', ticker='', field=''):
        """
            获取国内外指数的基本要素信息，包括指数名称、指数代码、发布机构、发布日期、基日、基点等。
        """
        code, result = self.client.getData(vs.IDX%(secID, ticker, field))
        return _ret_data(code, result)


    def IdxCons(self, secID='', ticker='', intoDate='', isNew='', field=''):
        """
            获取国内外指数的成分构成情况，包括指数成分股名称、成分股代码、入选日期、剔除日期等。
        """
        code, result = self.client.getData(vs.IDXCONS%(secID, ticker, intoDate, 
                                                       intoDate, isNew, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
