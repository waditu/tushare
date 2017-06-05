#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年06月04日
@author: debugo
@contact: me@debugo.com
'''
import re
import datetime


CFFEX_DAILY_URL = "http://www.cffex.com.cn/fzjy/mrhq/%s/%s/%s_1.csv"
SHFE_DAILY_URL = 'http://www.shfe.com.cn/data/dailydata/kx/kx%s.dat'
SHFE_VWAP_URL = 'http://www.shfe.com.cn/data/dailydata/ck/%sdailyTimePrice.dat'
DCE_DAILY_URL = "http://www.dce.com.cn//publicweb/quotesdata/dayQuotesCh.html"
CZCE_DAILY_URL = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/%s/%s/FutureDataDaily.txt'

CFFEX_COLUMNS = ['open','high','low','volume','turnover','open_interest','close','settle','change1','change2']
CZCE_COLUMNS = ['pre_close','open','high','low','close','settle','change1','change2','volume','open_interest','oi_chg','turnover','final_settle']
SHFE_COLUMNS =  {'CLOSEPRICE': 'close',  'HIGHESTPRICE': 'high', 'LOWESTPRICE': 'low', 'OPENINTEREST': 'open_interest', 'OPENPRICE': 'open',  'PRESETTLEMENTPRICE': 'pre_settle', 'SETTLEMENTPRICE': 'settle',  'VOLUME': 'volume'}
SHFE_VWAP_COLUMNS = {':B1': 'date', 'INSTRUMENTID': 'symbol', 'TIME': 'time_range', 'REFSETTLEMENTPRICE': 'vwap'}
DCE_COLUMNS = ['variety', 'month', 'open', 'high', 'low', 'close', 'pre_settle', 'settle', 'change1','change2','volume','open_interest','oi_chg','turnover']
OUTPUT_COLUMNS = ['symbol', 'date', 'open', 'high', 'low', 'close', 'pre_close', 'volume', 'open_interest', 'turnover', 'settle', 'pre_settle', 'variety']
CLOSE_LOC = 5
PRE_SETTLE_LOC = 11
PRE_CLOSE_LOC = 6

FUTURE_SYMBOL_PATTERN = re.compile(r'(^[A-Za-z]{1,2})[0-9]{3,4}')
DATE_PATTERN = re.compile(r'^([0-9]{4})[-/]?([0-9]{2})[-/]?([0-9]{2})')
SIM_HAEDERS = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
DCE_HEADERS = {
    'cache-control': "no-cache",
    'postman-token': "153f42ca-148a-8f03-3302-8172cc4a5185"
}
def convert_date(date):
    """
    transform a date string to datetime.date object.
    :param day, string, e.g. 2016-01-01, 20160101 or 2016/01/01
    :return: object of datetime.date(such as 2016-01-01) or None
    """
    if isinstance(date, datetime.date):
        return date
    elif isinstance(date, str):
        match = DATE_PATTERN.match(date)
        if match:
            groups = match.groups()
            if len(groups) == 3:
                return datetime.date(year=int(groups[0]), month=int(groups[1]), day=int(groups[2]))
    return None

DCE_MAP =  {
    '豆一': 'A',
    '豆二': 'B',
    '豆粕': 'M',
    '豆油': 'Y',
    '棕榈油': 'P',
    '玉米': 'C',
    '玉米淀粉': 'CS',
    '鸡蛋': 'JD',
    '纤维板': 'FB',
    '胶合板': 'BB',
    '聚乙烯': 'L',
    '聚氯乙烯': 'V',
    '聚丙烯': 'PP',
    '焦炭': 'J',
    '焦煤': 'JM',
    '铁矿石': 'I'
}

FUTURE_CODE={
    'IH': ('CFFEX', '上证50指数'),
    'IF': ('CFFEX', '沪深300指数'),
    'IC': ('CFFEX', '中证500指数'),
    'T': ('CFFEX', '10年期国债期货'),
    'TF': ('CFFEX', '5年期国债期货'),
    'CU': ('SHFE', '沪铜'),
    'AL': ('SHFE', '沪铝'),
    'ZN': ('SHFE', '沪锌'),
    'PB': ('SHFE', '沪铅'),
    'NI': ('SHFE', '沪镍'),
    'SN': ('SHFE', '沪锡'),
    'AU': ('SHFE', '沪金'),
    'AG': ('SHFE', '沪银'),
    'RB': ('SHFE', '螺纹钢'),
    'WR': ('SHFE', '线材'),
    'HC': ('SHFE', '热轧卷板'),
    'FU': ('SHFE', '燃油'),
    'BU': ('SHFE', '沥青'),
    'RU': ('SHFE', '橡胶'),
    'A': ('DCE', '豆一'),
    'B': ('DCE', '豆二'),
    'M': ('DCE', '豆粕'),
    'Y': ('DCE', '豆油'),
    'P': ('DCE', '棕榈油'),
    'C': ('DCE', '玉米'),
    'CS': ('DCE', '玉米淀粉'),
    'JD': ('DCE', '鸡蛋'),
    'FB': ('DCE', '纤维板'),
    'BB': ('DCE', '胶合板'),
    'L': ('DCE', '聚乙烯'),
    'V': ('DCE', '聚氯乙烯'),
    'PP': ('DCE', '聚丙烯'),
    'J': ('DCE', '焦炭'),
    'JM': ('DCE', '焦煤'),
    'I': ('DCE', '铁矿石'),
    'SR': ('CZCE', '白糖'),
    'CF': ('CZCE', '棉花'),
    'PM': ('CZCE', '普麦'),
    'WH': ('CZCE', '强麦'),
    'OI': ('CZCE', '菜籽油'),
    'PTA': ('CZCE', 'PTA'),
    'RI': ('CZCE', '早籼稻'),
    'LR': ('CZCE', '晚籼稻'),
    'MA': ('CZCE', '甲醇'),
    'FG': ('CZCE', '玻璃'),
    'RS': ('CZCE', '油菜籽'),
    'RM': ('CZCE', '籽粕'),
    'TC': ('CZCE', '动力煤'),
    'ZC': ('CZCE', '动力煤'),
    'JR': ('CZCE', '粳稻'),
    'SF': ('CZCE', '硅铁'),
    'SM': ('CZCE', '锰硅')
}
