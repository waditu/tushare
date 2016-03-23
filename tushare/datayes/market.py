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

class Market():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client


    def TickRTSnapshot(self, securityID='', field=''):
        """
            高频数据，获取一只或多只证券最新Level1股票信息。 输入一只或多只证券代码，
            如000001.XSHG (上证指数） 或000001.XSHE（平安银行）， 还有所选字段， 得到证券的最新交易快照。 
            证券可以是股票，指数， 部分债券或 基金。
        """
        code, result = self.client.getData(vs.TICKRTSNAPSHOT%(securityID, field))
        return _ret_data(code, result)


    def TickRTSnapshotIndex(self, securityID='', field=''):
        """
            高频数据，获取一个指数的成分股的最新Level1股票信息。 
            输入一个指数的证券代码，如000001.XSHG (上证指数） 或000300.XSHG（沪深300）， 
            还有所选字段， 得到指数成分股的最新交易快照。
        """
        code, result = self.client.getData(vs.TICKRTSNAPSHOTINDEX%(securityID, field))
        return _ret_data(code, result)


    def FutureTickRTSnapshot(self, instrumentID='', field=''):
        """
            高频数据，获取一只或多只期货的最新市场信息快照
        """
        code, result = self.client.getData(vs.FUTURETICKRTSNAPSHOT%(instrumentID, field))
        return _ret_data(code, result)


    def TickRTIntraDay(self, securityID='', endTime='', startTime='', field=''):
        """
            高频数据，获取一只证券当日内时间段的Level1信息。 证券可以是股票，指数， 部分债券或 基金。
        """
        code, result = self.client.getData(vs.TICKRTINTRADAY%(securityID, endTime, startTime, field))
        return _ret_data(code, result)


    def BarRTIntraDay(self, securityID='', endTime='', startTime='', field=''):
        """
            高频数据，获取一只证券当日的分钟线信息。 
            输入一只证券代码，如000001.XSHE（平安银行）， 得到此证券的当日的分钟线。 
            证券目前是股票，指数，基金和部分债券。分钟线的有效数据上午从09：30 到11：30，下午从13：01到15：00
        """
        code, result = self.client.getData(vs.BARRTINTRADAY%(securityID, endTime, startTime, field))
        return _ret_data(code, result)
    
    
    def BarHistIntraDay(self, securityID='', date='', endTime='', startTime='', field=''):
        """
            高频数据，获取一只证券历史的分钟线信息。 
            输入一只证券代码，如000001.XSHE（平安银行）， 得到此证券的当日的分钟线。 
            证券目前是股票，指数，基金和部分债券。分钟线的有效数据上午从09：30 到11：30，下午从13：01到15：00
        """
        code, result = self.client.getData(vs.BARHISTONEDAY%(securityID, date, endTime, startTime, field))
        return _ret_data(code, result)
    
    
    def BarHistDayRange(self, securityID='', startDate='', endDate='', field=''):
        code, result = self.client.getData(vs.BARHISTDAYRANGE%(securityID, startDate, endDate, field))
        return _ret_data(code, result)


    def FutureTickRTIntraDay(self, instrumentID='', endTime='', startTime='', field=''):
        """
            高频数据，获取一只期货在本清算日内某时间段的行情信息
        """
        code, result = self.client.getData(vs.FUTURETICKRTINTRADAY%(instrumentID, endTime, startTime, field))
        return _ret_data(code, result)
    
    
    def FutureBarsOneDay(self, instrumentID='', date='', field=''):
        code, result = self.client.getData(vs.FUTUREBARINDAY%(instrumentID, date, field))
        return _ret_data(code, result)
    
    
    def FutureBarsDayRange(self, instrumentID='', startDate='', endDate='', field=''):
        code, result = self.client.getData(vs.FUTUREBARDATERANGE%(instrumentID, startDate, endDate, field))
        return _ret_data(code, result)


    def StockFactorsOneDay(self, tradeDate='', secID='', ticker='', field=''):
        """
            高频数据，获取多只股票历史上某一天的因子数据
        """
        code, result = self.client.getData(vs.STOCKFACTORSONEDAY%(tradeDate, secID, ticker, field))
        return _ret_data(code, result)


    def StockFactorsDateRange(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            高频数据，获取一只股票历史上某一时间段的因子数据
        """
        code, result = self.client.getData(vs.STOCKFACTORSDATERANGE%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def SecTips(self, tipsTypeCD='', field=''):
        """
            上海证券交易所、深圳证券交易所今日停复牌股票列表。数据更新频率：日。
        """
        code, result = self.client.getData(vs.SECTIPS%(tipsTypeCD, field))
        return _ret_data(code, result)


    def BarRTIntraDayOneMinute(self, time='', field=''):
        """
            获取所有股票某一分钟的分钟线
        """
        code, result = self.client.getData(vs.BARRTINTRADAYONEMINUTE%(time, field))
        return _ret_data(code, result)


    def EquRTRank(self, desc='', exchangeCD='', field=''):
        """
            获取沪深股票涨跌幅排行
        """
        code, result = self.client.getData(vs.EQURTRANK%(desc, exchangeCD, field))
        return _ret_data(code, result)


    def MktMFutd(self, contractMark='', contractObject='', mainCon='', tradeDate='', endDate='', 
                 startDate='', field=''):
        """
            获取四大期货交易所主力合约、上海黄金交易所黄金(T+D)、白银(T+D)以及国外主要期货连续合约行情信息。 历史追溯至2006年，每日16:00更新。
        """
        code, result = self.client.getData(vs.MKTMFUTD%(contractMark, contractObject, mainCon, 
                                                        tradeDate, endDate, startDate, field))
        return _ret_data(code, result)


    def OptionTickRTSnapshot(self, optionId='', field=''):
        """
            高频数据，获取期权最新市场信息快照
        """
        code, result = self.client.getData(vs.OPTIONTICKRTSNAPSHOT%(optionId, field))
        return _ret_data(code, result)


    def FutureBarRTIntraDay(self, instrumentID='', endTime='', startTime='', field=''):
        """
            高频数据，获取当日期货分钟线
        """
        code, result = self.client.getData(vs.FUTUREBARRTINTRADAY%(instrumentID, endTime, startTime, field))
        return _ret_data(code, result)


    def IndustryTickRTSnapshot(self, securityID='', field=''):
        """
            获取行业（证监会行业标准）资金流向，内容包括小单成交金额、中单成交金额、大单成交金额、超大单成交金额、本次成交单总金额等。
        """
        code, result = self.client.getData(vs.INDUSTRYTICKRTSNAPSHOT%(securityID, field))
        return _ret_data(code, result)


    def MktEqudLately(self, field=''):
        """
            获取沪深股票个股最近一次日行情，默认日期区间是过去1年，包含昨收价、开盘价、最高价、最低价、收盘价、成交量、成交金额等字段，每日15:30更新
        """
        code, result = self.client.getData(vs.MKTEQUDLATELY%(field))
        return _ret_data(code, result)


    def MktEqud(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取沪深AB股日行情信息，默认日期区间是过去1年，包含昨收价、开盘价、最高价、最低价、收盘价、成交量、成交金额等字段，每日15:30更新
        """
        code, result = self.client.getData(vs.MKTEQUD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktHKEqud(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取香港交易所股票开、收、高、低，成交等日行情信息，每日17:00前更新
        """
        code, result = self.client.getData(vs.MKTHKEQUD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktBondd(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取债券交易开、收、高、低，成交等日行情信息，每日16:00前更新
        """
        code, result = self.client.getData(vs.MKTBONDD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktRepod(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取债券回购交易开、收、高、低，成交等日行情信息，每日16:00前更新
        """
        code, result = self.client.getData(vs.MKTREPOD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktFundd(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取基金买卖交易开、收、高、低，成交等日行情信息，每日16:00前更新。
        """
        code, result = self.client.getData(vs.MKTFUNDD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktFutd(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取四大期货交易所期货合约、上海黄金交易所黄金(T+D)、白银(T+D)以及国外主要期货连续合约行情信息。 默认日期区间是过去一年。日线数据第一次更新为交易结束后（如遇线路不稳定情况数据可能存在误差），第二次更新为18:00pm，其中主力合约是以连续三个交易日持仓量最大为基准计算的。
        """
        code, result = self.client.getData(vs.MKTFUTD%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktFutMTR(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取期货会员在各交易日期货合约的成交量、成交排名及成交量增减信息，每日16:00前更新。
        """
        code, result = self.client.getData(vs.MKTFUTMTR%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktFutMSR(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取期货会员在各交易日期货合约的空头持仓、排名及空头持仓增减信息，每日16:00前更新。
        """
        code, result = self.client.getData(vs.MKTFUTMSR%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktFutMLR(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取期货会员在各交易日期货合约的多头持仓、排名及多头持仓增减信息，每日16:00前更新。
        """
        code, result = self.client.getData(vs.MKTFUTMLR%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktIdxd(self, indexID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取指数日线行情信息，包含昨收价、开盘价、最高价、最低价、收盘价、成交量、成交金额等字段，默认日期区间是过去1年，其中沪深指数行情每日15:30更新。
        """
        code, result = self.client.getData(vs.MKTIDXD%(indexID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktBlockd(self, secID='', ticker='', tradeDate='', assetClass='', beginDate='', endDate='', field=''):
        """
            获取沪深交易所交易日大宗交易成交价，成交量等信息。
        """
        code, result = self.client.getData(vs.MKTBLOCKD%(secID, ticker, tradeDate, assetClass, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktOptd(self, optID='', secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            主要记录上交所期权行情，包含昨结算、昨收盘、开盘价、最高价、最低价、收盘价、结算价、成交量、成交金额、持仓量等字段，每日16:00前更新。
        """
        code, result = self.client.getData(vs.MKTOPTD%(optID, secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktEqudAdj(self, secID='', ticker='', tradeDate='', beginDate='', endDate='', field=''):
        """
            获取获取沪深A股和B股前复权日行情信息，包含前复权昨收价、前复权开盘价、前复权最高价、前复权最低价、前复权收盘价，每日开盘前更新数据。
        """
        code, result = self.client.getData(vs.MKTEQUDADJ%(secID, ticker, tradeDate, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktAdjf(self, secID='', ticker='', field=''):
        """
            获取获取沪深A股和B股用来调整行情的前复权因子数据，包含除权除息日、除权除息事项具体数据、本次复权因子、累积复权因子以及因子调整的截止日期。该因子用来调整历史行情，不作为预测使用，于除权除息日进行计算调整。
        """
        code, result = self.client.getData(vs.MKTADJF%(secID, ticker, field))
        return _ret_data(code, result)


    def MktFutdVol(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            获取四大期货交易所期货合约行情信息。 默认日期区间是过去一年。日线数据第一次更新为交易结束后（如遇线路不稳定情况数据可能存在误差），第二次更新为18:00pm，其中主力合约是以成交量最大为基准计算的。
        """
        code, result = self.client.getData(vs.MKTFUTDVOL%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


    def MktLimit(self, secID='', ticker='', tradeDate='', field=''):
        """
            主要记录盘前每日个股及基金涨跌停板价格，每日9:00更新
        """
        code, result = self.client.getData(vs.MKTLIMIT%(secID, ticker, tradeDate, field))
        return _ret_data(code, result)


    def MktFunddAdjAf(self, secID='', ticker='', beginDate='', endDate='', field=''):
        """
            主要记录基金每日后复权行情，包括开高低收、成交量、成交价格等
        """
        code, result = self.client.getData(vs.MKTFUNDDADJAF%(secID, ticker, beginDate, endDate, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None  
    
    