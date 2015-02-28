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
import lxml.html
from lxml import etree

def get_latest_news(top=ct.PAGE_NUM[2], show_content=False):
    """
        获取即时财经新闻
    
    Parameters
    --------
        top:数值，显示最新消息的条数，默认为80条
        show_content:是否显示新闻内容，默认False
    
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
                                                       'lnews'],top ,
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
            arow = [r['channel']['title'], r['title'], rtstr, r['url']]
            if show_content:
                arow.append(latest_content(r['url']))
            data.append(arow)
        df = pd.DataFrame(data, columns=nv.LATEST_COLS_C if show_content else nv.LATEST_COLS)
        return df
    except Exception as er:
        print str(er)


def latest_content(url):
    '''
        获取即时财经新闻内容
    Parameter
    --------
        url:新闻链接
    
    Return
    --------
        string:返回新闻的文字内容
    '''
    try:
        html = lxml.html.parse(url)
        res = html.xpath('//div[@id=\"artibody\"]/p')
        sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr).replace('&#12288;', '')#.replace('\n\n', '\n').
        html_content = lxml.html.fromstring(sarr)
        content = html_content.text_content()
        return content
    except Exception as er:
        print str(er)  

def _random(n=16):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))

