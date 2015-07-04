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


    def dy_master_tradeCal(self, exchangeCD='XSHG,XSHE', beginDate='',
                           endDate='', field=''):
        code, result = self.client.getData(vs.TRADE_DATE%(exchangeCD, beginDate,
                                                             endDate, field))
        return _ret_data(code, result)


    def dy_master_secID(self, ticker='000001', partyID='',
                        cnSpell='', assetClass='', field=''):
        code, result = self.client.getData(vs.SEC_ID%(ticker, partyID,
                                                             cnSpell, assetClass, field))
        return _ret_data(code, result)
    
    
    def dy_master_equInfo(self, ticker='wx', pagesize='10',
                        pagenum='1', field=''):
        code, result = self.client.getData(vs.EQU_INFO%(ticker, pagesize,
                                                             pagenum, field))
        return _ret_data(code, result)
    
    
    def dy_master_region(self, field=''):
        code, result = self.client.getData(vs.REGION%(field))
        return _ret_data(code, result)
    
    
    def dy_master_regionRel(self, ticker='', typeID='',
                        secID='', field=''):
        code, result = self.client.getData(vs.REGION_REL%(ticker, typeID,
                                                             secID, field))
        return _ret_data(code, result)
    
    
    def dy_master_secType(self, field=''):
        code, result = self.client.getData(vs.SEC_TYPE%(field))
        return _ret_data(code, result)
    
    
    def dy_master_secTypeRel(self, ticker='', typeID='101001004001001',
                        secID='', field=''):
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


