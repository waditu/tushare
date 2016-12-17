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

class Equity():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
        
    def Equ(self, equTypeCD='', secID='', ticker='', listStatusCD='', field=''):
        """
            获取股票的基本信息，包含股票交易代码及其简称、股票类型、上市状态、上市板块、上市日期等；上市状态为最新数据，不显示历史变动信息。
        """
        code, result = self.client.getData(vs.EQU%(equTypeCD, secID, ticker, listStatusCD, field))
        return _ret_data(code, result)


    def EquAllot(self, isAllotment='', secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取股票历次配股的基本信息，包含每次配股方案的内容、方案进度、历史配股预案公布次数以及最终是否配股成功。
        """
        code, result = self.client.getData(vs.EQUALLOT%(isAllotment, secID, ticker, 
                                                        beginDate, endDate, field))
        return _ret_data(code, result)


    def EquDiv(self, eventProcessCD='', exDivDate='', secID='', ticker='', beginDate='', 
               endDate='', field=''):
        """
            获取股票历次分红(派现、送股、转增股)的基本信息，包含历次分红预案的内容、实施进展情况以及历史宣告分红次数。
        """
        code, result = self.client.getData(vs.EQUDIV%(eventProcessCD, exDivDate, 
                                                      secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def EquIndustry(self, industry='', industryID='', industryVersionCD='', secID='', 
                    ticker='', intoDate='', field=''):
        """
            输入证券ID或股票交易代码，获取股票所属行业分类
        """
        code, result = self.client.getData(vs.EQUINDUSTRY%(industry, industryID, industryVersionCD, 
                                                           secID, ticker, intoDate, field))
        return _ret_data(code, result)


    def EquIPO(self, eventProcessCD='', secID='', ticker='', field=''):
        """
            获取股票首次公开发行上市的基本信息，包含股票首次公开发行的进程及发行结果。
        """
        code, result = self.client.getData(vs.EQUIPO%(eventProcessCD, secID, ticker, field))
        return _ret_data(code, result)


    def EquRef(self, secID='', ticker='', beginDate='', endDate='', eventProcessCD='', field=''):
        """
            获取股票股权分置改革的基本信息，包含股改进程、股改实施方案以及流通股的变动情况。
        """
        code, result = self.client.getData(vs.EQUREF%(secID, ticker, beginDate, endDate, 
                                                      eventProcessCD, field))
        return _ret_data(code, result)


    def EquRetud(self, listStatusCD='', secID='', ticker='', beginDate='', 
                 dailyReturnNoReinvLower='', dailyReturnNoReinvUpper='', 
                 dailyReturnReinvLower='', dailyReturnReinvUpper='', 
                 endDate='', isChgPctl='', field=''):
        """
            获取股票每日回报率的基本信息，包含交易当天的上市状态、日行情以及除权除息事项的基本数据。
        """
        code, result = self.client.getData(vs.EQURETUD%(listStatusCD, secID, ticker, 
                                                        beginDate, dailyReturnNoReinvLower, 
                                                        dailyReturnNoReinvUpper, 
                                                        dailyReturnReinvLower, 
                                                        dailyReturnReinvUpper, 
                                                        endDate, isChgPctl, field))
        return _ret_data(code, result)


    def EquSplits(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取股票进行股本拆细或者缩股的基本信息。
        """
        code, result = self.client.getData(vs.EQUSPLITS%(secID, ticker, beginDate, 
                                                         endDate, field))
        return _ret_data(code, result)


    def FstTotal(self, beginDate='', endDate='', exchangeCD='', field=''):
        """
            获取上海、深圳交易所公布的每个交易日的融资融券交易汇总的信息，包括成交量、成交金额。本交易日可获取前一交易日的数据。
        """
        code, result = self.client.getData(vs.FSTTOTAL%(beginDate, endDate, 
                                                        exchangeCD, field))
        return _ret_data(code, result)


    def FstDetail(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取上海、深圳交易所公布的每个交易日的融资融券交易具体的信息，包括标的证券信息、融资融券金额以及数量方面的数据。本交易日可获取前一交易日的数据。
        """
        code, result = self.client.getData(vs.FSTDETAIL%(secID, ticker, 
                                                         beginDate, endDate, field))
        return _ret_data(code, result)


    def EquShare(self, secID='', ticker='', beginDate='', endDate='', 
                 partyID='', field=''):
        """
            获取上市公司股本结构及历次股本变动数据。
        """
        code, result = self.client.getData(vs.EQUSHARE%(secID, ticker, 
                                                        beginDate, endDate, 
                                                        partyID, field))
        return _ret_data(code, result)


    def SecST(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            通过输入股票ID（通联编制）或股票交易代码（支持多值输入，最大支持50只），选择查询开始日期与结束日期，获取股票在一段时间ST标记信息。
        """
        code, result = self.client.getData(vs.SECST%(secID, ticker, 
                                                     beginDate, endDate, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    

