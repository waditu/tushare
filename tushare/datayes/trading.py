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

class Trading():
    
    def __init__(self, client):
        self.client = client
        
    def dy_market_tickRT(self, securityID='000001.XSHG,000001.XSHE', field=vs.TICK_RT_DEFAULT_COLS):
        """
        获取最新市场信息快照
        获取一只或多只证券最新Level1股票信息。 
        输入一只或多只证券代码，如000001.XSHG (上证指数） 或000001.XSHE（平安银行）， 
        还有所选字段， 得到证券的最新交易快照。 
        证券可以是股票，指数， 部分债券或 基金。
        getTickRTSnapshot
        """
        code, result = self.client.getData(vs.TICK_RT%(securityID, field))
        return _ret_data(code, result)
    
    
    def dy_market_tickRtIndex(self, securityID='', field=''):
        """
        获取指数成份股的最新市场信息快照 
        获取一个指数的成份股的最新Level1股票信息。 
        输入一个指数的证券代码，如000001.XSHG (上证指数） 或000300.XSHG（沪深300）， 
        还有所选字段， 得到指数成份股的最新交易快照。
        getTickRTSnapshotIndex
        """
        code, result = self.client.getData(vs.TICK_RT_INDEX%(securityID, field))
        return _ret_data(code, result)
    
    
    def dy_market_industry_rt(self, securityID='', field=''):
        """
        获取行业（证监会行业标准）资金流向
        内容包括小单成交金额、中单成交金额、大单成交金额、超大单成交金额、本次成交单总金额等。
        getIndustryTickRTSnapshot
        """
        code, result = self.client.getData(vs.INDUSTRY_TICK_RT%(securityID, field))
        return _ret_data(code, result)
    
    
    def dy_market_future_rt(self, instrumentID='', field=''):
        """
        获取一只或多只期货的最新市场信息快照
        getFutureTickRTSnapshot
        """
        code, result = self.client.getData(vs.FUTURE_TICK_RT%(instrumentID, field))
        return _ret_data(code, result)
    
    
    def dy_market_equ_rtrank(self, exchangeCD='', pagesize='',
                             pagenum='', desc='', field=''):
        """
        获取沪深股票涨跌幅排行
        getEquRTRank
        """
        code, result = self.client.getData(vs.EQU_RT_RANK%(exchangeCD, pagesize,
                                                            pagenum, desc, field))
        return _ret_data(code, result)
    
    
    def dy_market_option_rt(self, optionId='', field=''):
        """
        获取期权最新市场信息快照
        getOptionTickRTSnapshot
        """
        code, result = self.client.getData(vs.OPTION_RT%(optionId, field))
        return _ret_data(code, result)
    
    
    def dy_market_sectips(self, tipsTypeCD='H', field=''):
        """
        上海证券交易所、深圳证券交易所今日停复牌股票列表。数据更新频率：日。
        getSecTips
        """
        code, result = self.client.getData(vs.SEC_TIPS%(tipsTypeCD, field))
        return _ret_data(code, result)
    
    
    def dy_market_tickrt_intraday(self, securityID='000001.XSHE', startTime='',
                             endTime='', field=''):
        """
        获取一只股票，指数，债券，基金在当日内时间段Level1信息 
        对应：getTickRTIntraDay
        """
        code, result = self.client.getData(vs.TICK_RT_INTRADAY%(securityID, startTime,
                                                            endTime, field))
        return _ret_data(code, result)
    
    
    def dy_market_bar_rt(self, securityID='000001.XSHE', startTime='',
                             endTime='', unit='1', field=''):
        """
        获取一只证券当日的分钟线信息。 
        输入一只证券代码，如000001.XSHE（平安银行）， 得到此证券的当日的分钟线。 
        证券目前是股票，指数，基金和部分债券。
        分钟线的有效数据上午从09：30 到11：30，下午从13：01到15：00
        对应：getBarRTIntraDay
        """
        code, result = self.client.getData(vs.TICK_RT_INTRADAY%(securityID, startTime,
                                                            endTime, field))
        return _ret_data(code, result)
    
def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
