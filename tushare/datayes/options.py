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

class Options():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def Opt(self, contractStatus='', optID='', secID='', ticker='', varSecID='', varticker='', field=''):
        """
            获取期权合约编码，交易代码，交易市场，标的等相关信息
        """
        code, result = self.client.getData(vs.OPT%(contractStatus, optID, secID, ticker, 
                                                   varSecID, varticker, field))
        return _ret_data(code, result)


    def OptVar(self, exchangeCD='', secID='', ticker='', contractType='', exerType='', field=''):
        """
            获取期权品种名称、生效日期、履约方式、交割方式、申报单位等相关信息。
        """
        code, result = self.client.getData(vs.OPTVAR%(exchangeCD, secID, ticker, 
                                                      contractType, exerType, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None  
    
