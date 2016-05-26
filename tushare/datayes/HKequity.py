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

class HKequity():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def HKEqu(self, listStatusCD='', secID='', ticker='', field=''):
        """
            获取香港交易所上市股票的基本信息，包含股票交易代码及其简称、股票类型、上市状态、上市板块、上市日期等；上市状态为最新状态。
        """
        code, result = self.client.getData(vs.HKEQU%(listStatusCD, secID, ticker, field))
        return _ret_data(code, result)


    def HKEquCA(self, secID='', ticker='', eventTypeCD='', field=''):
        """
            获取香港交易所上市公司行为，包含有首发、现金增资、分红、拆细等。
        """
        code, result = self.client.getData(vs.HKEQUCA%(secID, ticker, eventTypeCD, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
