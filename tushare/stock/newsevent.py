# -*- coding:utf-8 -*-

"""
新闻事件数据接口 
Created on 2015/02/07
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import urllib2
from tushare.stock import cons as ct
from tushare.stock import news_vars as nv
import demjson
import pandas as pd
from datetime import datetime


def get_latest_news():
    """
        获取即时财经新闻
    Return
    --------
    DataFrame
        classify :新闻类别
        title :新闻标题
        time :发布时间
        url :新闻链接
    """
    try:
        request = urllib2.Request(nv.LATEST_URL % (ct.P_TYPE['http'], ct.DOMAINS['sina'],
                                                   ct.PAGES[
                                                       'lnews'], ct.PAGE_NUM[2],
                                                   _random()))
        data_str = urllib2.urlopen(request, timeout=10).read()
        data_str = data_str.decode('GBK')
        data_str = data_str.split('=')[1][:-1]
        data_str = demjson.decode(data_str)
        data_str = data_str['list']
        data = []
        for r in data_str:
            rt = datetime.fromtimestamp(r['time'])
            rtstr = datetime.strftime(rt, "%m-%d %H:%M")
            data.append([r['channel']['title'], r['title'], rtstr, r['url']])
        df = pd.DataFrame(data, columns=nv.LATEST_COLS)
        return df
    except Exception as er:
        print str(er)


def _random(n=16):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))

