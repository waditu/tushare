#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Created on 2015年7月4日
@author: JimmyLiu
@QQ:52799046
"""
from tushare.datayes import vars as vs
import pandas as pd
from pandas.compat import StringIO

class Basics():
    
    def __init__(self , client):
        self.client = client


    def dy_master_secID(self, ticker='000001', partyID='',
                        cnSpell='', assetClass='', field=''):
        """
        证券编码及基本上市信息
        getSecID
        输入一个或多个证券交易代码，获取证券ID，证券在数据结构中的一个唯一识别的编码；
        同时可以获取输入证券的基本上市信息，如交易市场，上市状态，交易币种，ISIN编码等。
        """
        code, result = self.client.getData(vs.SEC_ID%(ticker, partyID,
                                                             cnSpell, assetClass, field))
        return _ret_data(code, result)
    
    
    def dy_master_tradeCal(self, exchangeCD='XSHG,XSHE', beginDate='',
                           endDate='', field=''):
        """
        交易所交易日历
        getTradeCal
        输入交易所，选取日期范围，可查询获取日历日期当天是否开市信息
        """
        code, result = self.client.getData(vs.TRADE_DATE%(exchangeCD, beginDate,
                                                             endDate, field))
        return _ret_data(code, result)

    
    def dy_master_equInfo(self, ticker='wx', pagesize='10',
                        pagenum='1', field=''):
        """
        沪深股票键盘精灵
        getEquInfo
        根据拼音或股票代码，匹配股票代码、名称。包含正在上市的全部沪深股票。
        """
        code, result = self.client.getData(vs.EQU_INFO%(ticker, pagesize,
                                                             pagenum, field))
        return _ret_data(code, result)
    
    
    def dy_master_region(self, field=''):
        """
        获取中国地域分类，以行政划分为标准。
        getSecTypeRegion
        """
        code, result = self.client.getData(vs.REGION%(field))
        return _ret_data(code, result)
    
    
    def dy_master_regionRel(self, ticker='', typeID='',
                        secID='', field=''):
        """
        获取沪深股票地域分类，以注册地所在行政区域为标准。
        getSecTypeRegionRel
        """
        code, result = self.client.getData(vs.REGION_REL%(ticker, typeID,
                                                             secID, field))
        return _ret_data(code, result)
    
    
    def dy_master_secType(self, field=''):
        """
        证券分类列表
        一级分类包含有沪深股票、港股、基金、债券、期货、期权等，每个分类又细分有不同类型；
        可一次获取全部分类。
        getSecType
        """
        code, result = self.client.getData(vs.SEC_TYPE%(field))
        return _ret_data(code, result)
    
    
    def dy_master_secTypeRel(self, ticker='', typeID='101001004001001',
                        secID='', field=''):
        """
        录证券每个分类的成分，证券分类可通过在getSecType获取。
        getSecTypeRel
        """
        code, result = self.client.getData(vs.SEC_TYPE_REL%(ticker, typeID,
                                                             secID, field))
        return _ret_data(code, result)
    
    
def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None

