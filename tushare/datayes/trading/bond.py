#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Created on 2015年7月31日
@author: Jimmy Liu
@group: DataYes Data.dept
@QQ:52799046
"""
from tushare.datayes.common import vars as vs 
import pandas as pd
from pandas.compat import StringIO

class Bond():
    
    def __init__(self, client):
        self.client = client
        
        
    def Bond(self, secID='', ticker='', field=''):
        """
            债券的基本面信息，涵盖了债券计息方式、付息频率、起息日、到期日、兑付形式等。
        """
        code, result = self.client.getData(vs.BOND%(secID, ticker, field))
        return _ret_data(code, result)
    

    def BondCf(self, secID='', ticker='', beginDate='', cashTypeCD='', 
               endDate='', field=''):
        """
            债券在每个计息周期付息兑付的相关数据。日期区间默认为过去一年。
        """
        code, result = self.client.getData(vs.BONDCF%(secID, ticker, 
                                                      beginDate, cashTypeCD, endDate, field))
        return _ret_data(code, result)


    def BondCoupon(self, secID='', ticker='', field=''):
        """
            固定利率债券、浮动利率债券每个计息周期的票面利率，包括分段计息的具体利率。
        """
        code, result = self.client.getData(vs.BONDCOUPON%(secID, ticker, field))
        return _ret_data(code, result)


    def BondGuar(self, secID='', ticker='', guarModeCD='', field=''):
        """
            收录债券担保信息，如担保人、担保类型、担保方式、担保期限等。
        """
        code, result = self.client.getData(vs.BONDGUAR%(secID, ticker, guarModeCD, field))
        return _ret_data(code, result)


    def BondIssue(self, secID='', ticker='', raiseModeCD='', field=''):
        """
            债券在一级市场发行信息，记录的要素包括有发行方式、发行价格、当次发行规模等
        """
        code, result = self.client.getData(vs.BONDISSUE%(secID, ticker, raiseModeCD, field))
        return _ret_data(code, result)


    def BondOption(self, secID='', ticker='', field=''):
        """
            记录债券在发行时约定在存续期内投资人或发行人可行使的选择权，如债券回售、债券赎回等。
        """
        code, result = self.client.getData(vs.BONDOPTION%(secID, ticker, field))
        return _ret_data(code, result)


    def BondRating(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            债券的长期评级、短期评级以及历史评级变动记录。
        """
        code, result = self.client.getData(vs.BONDRATING%(secID, ticker, beginDate, 
                                                          endDate, field))
        return _ret_data(code, result)


    def GuarRating(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            各评级机构公布的债券担保人的信用评级数据及历史变动记录。
        """
        code, result = self.client.getData(vs.GUARRATING%(secID, ticker, beginDate, 
                                                          endDate, field))
        return _ret_data(code, result)


    def IssuerRating(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            各评级机构公布的债券发行人的信用评级数据及历史变动记录。
        """
        code, result = self.client.getData(vs.ISSUERRATING%(secID, ticker, beginDate, 
                                                            endDate, field))
        return _ret_data(code, result)


    def Repo(self, secID='', ticker='', field=''):
        """
            债券回购基本面信息，涵盖了回购交易代码、回购期限、申报价格最小变动单位(RMB)、申报参与价格单位(RMB)等。
        """
        code, result = self.client.getData(vs.REPO%(secID, ticker, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
