# -*- coding:utf-8 -*- 
"""
交易数据接口
"""
import time
import json
import urllib2
import pandas as pd
from tushare.stock import cons as ct
from pandas.io.common import urlopen
from pandas.util.testing import _network_error_classes
import re

def get_hist_data(code=None, start=None, end=None, retry_count=3,
                   pause=0.001):
    """
        获取个股历史交易记录
    Parameters
     ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取到API所提供的最早日期数据
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取到最近一个交易日数据
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 Number of times to retry query request.
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    return
      -------
      DataFrame
          属性:日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率
    """
    if code is None or len(code)!=6:
        return None
    symbol = code_to_symbol(code)
    url = ct.DAY_PRICE_URL%symbol
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            with urlopen(url) as resp:
                lines = resp.read()
        except _network_error_classes:
            pass
        else:
            js = json.loads(lines)
            df = pd.DataFrame(js['record'],columns=ct.DAY_PRICE_COLUMNS)
            df = df.applymap(lambda x: x.replace(u',', u''))#删除千位分隔符,
            df = df.drop('price_change',axis=1)
            df = df.set_index(['date']) 
            if start is not None:
                df = df.ix[df.index>=start]
            if end is not None:
                df = df.ix[df.index<=end]
            return df
    raise IOError("%s获取失败，请检查网络和URL:%s" % (code, url))

def _parsing_dayprice_json(pageNum=0):
    """
           处理当日行情分页数据，格式为json
     Parameters
     ------
        pageNum:页码
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
    """
    url = ct.SINA_DAY_PRICE_URL%pageNum
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()
    if text == 'null':
        return None
    reg = re.compile(r'\,(.*?)\:') 
    #修改成read_json能读入的json格式
    text = reg.sub(r',"\1":', text) 
    text = text.replace('"{symbol','{"symbol')
    text = text.replace('{symbol','{"symbol"')
    jstr = json.dumps(text,encoding='GBK')
    js = json.loads(jstr)
    df = pd.DataFrame(pd.read_json(js,dtype={'code':object}),columns=ct.DAY_TRADING_COLUMNS)
    #删除原始数据的symbol属性
    df = df.drop('symbol',axis=1)
    #删除停牌的股票
    df = df.ix[df.volume>0]
    return df
    
def get_today_all():
    """
        一次性获取最近一个日交易日所有股票的交易数据
    return
      -------
      DataFrame
           属性：代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率
    """
    df = _parsing_dayprice_json(1)
    if df is not None:
        for i in range(2,ct.DAY_PRICE_PAGES):
            newdf = _parsing_dayprice_json(i)
            df = df.append(newdf,ignore_index=True)
    return df

def code_to_symbol(code):
    """
        生成symbol代码标志
    """
    symbol = 'sh'+code if code[:1]=='6' else 'sz'+code
    return symbol
