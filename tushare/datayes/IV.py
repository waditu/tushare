# -*- coding:utf-8 -*- 
"""
通联数据
Created on 2015/10/12
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

from pandas.compat import StringIO
import pandas as pd
from tushare.util import vars as vs
from tushare.util.common import Client
from tushare.util import upass as up

class IV():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
        
    def DerIv(self, beginDate='', endDate='', optID='', SecID='', field=''):
        """
            原始隐含波动率,包括期权价格、累计成交量、持仓量、隐含波动率等。
        """
        code, result = self.client.getData(vs.DERIV%(beginDate, endDate, optID, SecID, field))
        return _ret_data(code, result)


    def DerIvHv(self, beginDate='', endDate='', SecID='', period='', field=''):
        """
            历史波动率，各个时间段的收盘－收盘历史波动率。
        """
        code, result = self.client.getData(vs.DERIVHV%(beginDate, endDate, SecID, period, field))
        return _ret_data(code, result)


    def DerIvIndex(self, beginDate='', endDate='', SecID='', period='', field=''):
        """
            隐含波动率指数，衡量30天至1080天到期平价期权的平均波动性的主要方法。
        """
        code, result = self.client.getData(vs.DERIVINDEX%(beginDate, endDate, SecID, period, field))
        return _ret_data(code, result)


    def DerIvIvpDelta(self, beginDate='', endDate='', SecID='', delta='', period='', field=''):
        """
            隐含波动率曲面(基于参数平滑曲线)，基于delta（0.1至0.9,0.05升步）和到期日（1个月至3年）而标准化的曲面。
        """
        code, result = self.client.getData(vs.DERIVIVPDELTA%(beginDate, endDate, SecID, delta, period, field))
        return _ret_data(code, result)


    def DerIvParam(self, beginDate='', endDate='', SecID='', expDate='', field=''):
        """
            隐含波动率参数化曲面，由二阶方程波动曲线在每个到期日平滑后的曲面（a,b,c曲线系数）
        """
        code, result = self.client.getData(vs.DERIVPARAM%(beginDate, endDate, SecID, expDate, field))
        return _ret_data(code, result)


    def DerIvRawDelta(self, beginDate='', endDate='', SecID='', delta='', period='', field=''):
        """
            隐含波动率曲面(基于原始隐含波动率)，基于delta（0.1至0.9,0.05升步）和到期日（1个月至3年）而标准化的曲面。
        """
        code, result = self.client.getData(vs.DERIVRAWDELTA%(beginDate, endDate, SecID, delta, period, field))
        return _ret_data(code, result)


    def DerIvSurface(self, beginDate='', endDate='', SecID='', contractType='', field=''):
        """
            隐含波动率曲面(在值程度)，基于在值程度而标准化的曲面。执行价格区间在-60%到+60%，5%升步，到期区间为1个月至3年。
        """
        code, result = self.client.getData(vs.DERIVSURFACE%(beginDate, endDate, SecID, contractType, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
