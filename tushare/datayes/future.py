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

class Future():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def Futu(self, exchangeCD='', secID='', ticker='', contractObject='', field=''):
        """
            获取国内四大期货交易所期货合约的基本要素信息，
            包括合约名称、合约代码、合约类型、合约标的、报价单位、最小变动价位、涨跌停板幅度、交易货币、
            合约乘数、交易保证金、上市日期、最后交易日、交割日期、交割方式、交易手续费、交割手续费、挂牌基准价、合约状态等。
        """
        code, result = self.client.getData(vs.FUTU%(exchangeCD, secID, ticker, contractObject, field))
        return _ret_data(code, result)


    def FutuConvf(self, secID='', ticker='', field=''):
        """
            获取国债期货转换因子信息，包括合约可交割国债名称、可交割国债交易代码、转换因子等。
        """
        code, result = self.client.getData(vs.FUTUCONVF%(secID, ticker, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
