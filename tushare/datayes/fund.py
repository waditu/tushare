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


class Fund():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
        
        
    def Fund(self, etfLof='', listStatusCd='', secID='', ticker='', category='', 
             operationMode='', field=''):
        """
            获取基金的基本档案信息，包含基金名称、交易代码、分级情况、所属类别、保本情况、上市信息、相关机构、投资描述等信息。
            收录了2005年以来的历史数据，数据更新频率为不定期。
        """
        code, result = self.client.getData(vs.FUND%(etfLof, listStatusCd, secID, 
                                                    ticker, category, operationMode, field))
        return _ret_data(code, result)


    def FundNav(self, dataDate='', secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取某只基金的历史净值数据(货币型、短期理财债券型除外),包括了单位份额净值、累计净值与复权净值。
            收录了2005年以来的历史数据，数据更新频率为日。不输入日期则默认获取近一年以来的历史数据。
        """
        code, result = self.client.getData(vs.FUNDNAV%(dataDate, secID, ticker, 
                                                       beginDate, endDate, field))
        return _ret_data(code, result)


    def FundDivm(self, dataDate='', secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取某只货币型基金或短期理财债券型基金的历史收益情况，包含了每万份收益，七日年化收益率等信息。
            收录了2005年以来的历史数据，数据更新频率为日。不输入日期则默认获取近一年以来的历史数据。
        """
        code, result = self.client.getData(vs.FUNDDIVM%(dataDate, secID, ticker, 
                                                        beginDate, endDate, field))
        return _ret_data(code, result)


    def FundDiv(self, secID='', ticker='', adjustedType='', beginDate='', endDate='', field=''):
        """
            获取基金的净值调整信息，包括基金分红和基金拆分两种调整情况。分红包含每份分红，除息日，分红在投资日；拆分包含份额折算比例，拆分日。
            收录了2005年以来的历史数据，数据更新频率为不定期。
        """
        code, result = self.client.getData(vs.FUNDDIV%(secID, ticker, adjustedType, 
                                                       beginDate, endDate, field))
        return _ret_data(code, result)


    def FundAssets(self, reportDate='', secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取基金定期披露的资产配置情况，包含了资产总值、资产净值，以及资产总值中权益类、固定收益类、现金及其他四种资产的市值与占比情况。
            收录了2005年以来的历史数据，数据更新频率为季度。获取方式支持：
            1）输入一个或多个secID/ticker，并输入beginDate和endDate，可以查询到指定基金，一段时间的资产配置；
            2）输入reportDate,不输入其他参数，可以查询到输入日期的全部基金资产配置
        """
        code, result = self.client.getData(vs.FUNDASSETS%(reportDate, secID, ticker, 
                                                          beginDate, endDate, field))
        return _ret_data(code, result)


    def FundHoldings(self, reportDate='', secID='', ticker='', beginDate='', endDate='', 
                     secType='', field=''):
        """
            获取基金定期披露的持仓明细，包含所持有的股票、债券、基金的持仓明细数据。收录了2005年以来的历史数据，数据更新频率为季度。获取方式支持：
            1）输入一个或多个secID/ticker，并输入beginDate和endDate，可以查询到指定基金，一段时间的基金持仓；
            2）输入reportDate,不输入其他参数，可以查询到输入日期的全部基金持仓数据。
        """
        code, result = self.client.getData(vs.FUNDHOLDINGS%(reportDate, secID, ticker, 
                                                            beginDate, endDate, secType, field))
        return _ret_data(code, result)


    def FundETFPRList(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取ETF基金交易日的申赎清单基本信息，包含标的指数名称，上一交易日的现金差额、最小申赎单位净值、
            单位净值，交易日当日的预估现金差额、最小申赎单位、现金替代比例上限、是否允许申购赎回、是否公布IOPV等信息。
            收录了2005年以来的历史数据，数据更新频率为日。不输入日期则默认获取近两天的数据。
        """
        code, result = self.client.getData(vs.FUNDETFPRLIST%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def FundETFCons(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取ETF基金每个交易日的跟踪的标的指数成分券清单，包含成分券的代码、简称、股票数量、现金替代溢价比、固定替代金额等信息。
            收录了2005年以来的历史数据，数据更新频率为日。不输入日期则默认获取近两天的数据。
        """
        code, result = self.client.getData(vs.FUNDETFCONS%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def FundRating(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取上海证券基金评级信息。收录了10年以来的历史数据，数据更新频率为月。不输入日期则默认获取近一年以来的历史数据。
        """
        code, result = self.client.getData(vs.FUNDRATING%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def FundSharesChg(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取场内基金的份额变动信息，包含基金名称、交易代码、交易市场、截止日期、流通份额等信息。收录了2005年以来的历史数据，数据更新频率为日。
        """
        code, result = self.client.getData(vs.FUNDSHARESCHG%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def FundLeverageInfo(self, exchangeCDLeverage='', secID='', ticker='', field=''):
        """
            获取分级基金的基本信息，包含母、子基金名称、交易代码、分拆比例、折算等信息。
        """
        code, result = self.client.getData(vs.FUNDLEVERAGEINFO%(exchangeCDLeverage, secID, ticker, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None   
    
