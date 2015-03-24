# -*- coding:utf-8 -*- 
"""
投资参考数据接口 
Created on 2015/03/21
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

from tushare.stock import cons as ct
from tushare.stock import ref_vars as rv
from tushare.util import dateutil as dt
import pandas as pd
import time
import lxml.html
from lxml import etree
import re
from pandas.util.testing import _network_error_classes

def get_divis(year=2014, top=25, 
              retry_count=3, pause=0.001):
    """
    获取分配预案数据
    Parameters
    --------
    year:年份
    top:取最新n条数据，默认取最近公布的25条
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    returns
    -------
    DataFrame
    code:股票代码
    name:股票名称
    year:分配年份
    report_date:公布日期
    divi:分红金额（每10股）
    shares:转增和送股数（每10股）
    """
    if top <= 25:
        df,pages = _dist_cotent(year, 0, retry_count, pause)
        return df.head(top)
    elif top == 'all':
        df,pages = _dist_cotent(year, 0, retry_count, pause)
        for idx in xrange(1,int(pages)):
            df = df.append(_dist_cotent(year, idx, retry_count,
                                        pause), ignore_index=True)
        return df
    else:
        if isinstance(top, int):
            allPages = top/25+1 if top%25>0 else top/25
            df,pages = _dist_cotent(year, 0, retry_count, pause)
            if allPages < pages:
                pages = allPages
            for idx in xrange(1,int(pages)):
                df = df.append(_dist_cotent(year, idx, retry_count,
                                            pause), ignore_index=True)
            return df.head(top)
        else:
            print 'top有误，请输入整数或all.'
    

def _fun_divi(x):
    reg = re.compile(ur'分红(.*?)元', re.UNICODE)
    res = reg.findall(x)
    return 0 if len(res)<1 else float(res[0])

def _fun_into(x):
    reg1 = re.compile(ur'转增(.*?)股', re.UNICODE)
    reg2 = re.compile(ur'送股(.*?)股', re.UNICODE)
    res1 = reg1.findall(x)
    res2 = reg2.findall(x)
    res1 = 0 if len(res1)<1 else float(res1[0])
    res2 = 0 if len(res2)<1 else float(res2[0])
    return res1 + res2
    
    
def _dist_cotent(year, pageNo, retry_count, pause):
    url = rv.DP_163_URL%(ct.P_TYPE['http'], ct.DOMAINS['163'],
                     ct.PAGES['163dp'], year, pageNo)
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            if pageNo>0:
                print rv.DP_MSG%pageNo
            html = lxml.html.parse(url)  
            res = html.xpath('//div[@class=\"fn_rp_list\"]/table')
            sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            df = pd.read_html(sarr, skiprows=[0])[0]
            df = df.drop(df.columns[0],axis=1)
            df.columns = rv.DP_163_COLS
            df['divi'] = df['plan'].map(_fun_divi)
            df['shares'] = df['plan'].map(_fun_into)
            df = df.drop('plan', axis=1)
            df['code'] = df['code'].astype(object)
            df['code'] = df['code'].map(lambda x : str(x).zfill(6))
            if pageNo == 0:
                page = html.xpath('//div[@class=\"mod_pages\"]/a')
                asr = page[len(page)-2]
                pages = asr.xpath('text()')
        except _network_error_classes:
            pass
        else:
#             df = df.drop_duplicates('code')
            if pageNo == 0:
                return df, pages[0]
            else:
                return df
    raise IOError("获取失败，请检查网络和URL:%s" % url)    
