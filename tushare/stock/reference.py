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
from tushare.util import dateu as dt
import pandas as pd
import time
import lxml.html
from lxml import etree
from pandas.io.common import urlopen
import re
import json
from pandas.util.testing import _network_error_classes

def profit_data(year=2014, top=25, 
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
            df = df.drop(df.columns[0], axis=1)
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
            if pageNo == 0:
                return df, pages[0]
            else:
                return df
    raise IOError("获取失败，请检查网络和URL:%s" % url)    


def forecast_data(year, quarter):
    """
        获取业绩预告数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        type,业绩变动类型【预增、预亏等】
        report_date,发布日期
        pre_eps,上年同期每股收益
        range,业绩变动范围
        
    """
    if _check_input(year,quarter) is True:
        data =  _get_forecast_data(year,quarter,1,[])
        df = pd.DataFrame(data,columns=ct.FORECAST_COLS)
        return df


def _get_forecast_data(year, quarter, pageNo, dataArr):
    url = ct.FORECAST_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], ct.PAGES['fd'], year,
                           quarter, pageNo, ct.PAGE_NUM[1])
    print 'getting data %s ...'%pageNo
    try:
        html = lxml.html.parse(url)
        xtrs = html.xpath("//table[@class=\"list_table\"]/tr")
        for trs in xtrs:
            code = trs.xpath('td[1]//span/a/text()')[0]
            name = trs.xpath('td[2]/span/a/text()')[0]
            type = trs.xpath('td[3]/a/text()')
            type = type[0] if len(type)>0 else trs.xpath('td[3]/text()')[0]
            report_date = trs.xpath('td[4]/text()')[0] 
            pre_eps = trs.xpath('td[7]/text()')[0] 
            pre_eps = '0' if pre_eps == '--' else pre_eps
            range = trs.xpath('td[8]/text()')[0] 
            dataArr.append([code,name,type,report_date,pre_eps,range])
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick') #获取下一页
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_forecast_data(year,quarter,pageNo,dataArr)
        else:
            return dataArr
    except:
        pass
    

def xsg_data(year=None, month=None, 
            retry_count=3, pause=0.001):
    """
    获取限售股解禁数据
    Parameters
    --------
    year:年份,默认为当前年
    month:解禁月份，默认为当前月
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    name:名称
    date:解禁日期
    count:解禁数量（万股）
    ratio:占总盘比率
    """
    year = dt.get_year() if year is None else year
    month = dt.get_month() if month is None else month
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            with urlopen(rv.XSG_URL%(ct.P_TYPE['http'], ct.DOMAINS['em'],
                                     ct.PAGES['emxsg'], year, month)) as resp:
                lines = resp.read()
        except _network_error_classes:
            pass
        else:
            da = lines[3:len(lines)-3]
            list =  []
            for row in da.split('","'):
                list.append([data for data in row.split(',')])
            df = pd.DataFrame(list)
            df = df[[1, 3, 4, 5, 6]]
            for col in [5, 6]:
                df[col] = df[col].astype(float)
            df[5] = df[5]/10000
            df[6] = df[6]*100
            df[5] = df[5].map(ct.FORMAT)
            df[6] = df[6].map(ct.FORMAT)
            df.columns = rv.XSG_COLS
            return df
    raise IOError("获取失败，请检查网络和URL")   


def fund_holdings(year, quarter,
                  retry_count=3, pause=0.001):
    """
    获取基金持股数据
    Parameters
    --------
    year:年份e.g 2014
    quarter:季度（只能输入1，2，3，4这个四个数字）
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    name:名称
    date:报告日期
    nums:基金家数
    nlast:与上期相比（增加或减少了）
    count:基金持股数（万股）
    clast:与上期相比
    amount:基金持股市值
    ratio:占流通盘比率
    """
    start,end = rv.QUARTS_DIC[str(quarter)]
    if quarter == 1:
        start = start % str(year-1)
        end = end%year
    else:
        start, end = start%year, end%year
    df, pages = _holding_cotent(start, end, 0, retry_count, pause)
    for idx in xrange(1, pages):
        df = df.append(_holding_cotent(start, end, idx, retry_count, pause),
                  ignore_index=True)
    print df

def _holding_cotent(start, end, pageNo, retry_count, pause):
    url = rv.FUND_HOLDS_URL%(ct.P_TYPE['http'], ct.DOMAINS['163'],
                     ct.PAGES['163fh'], ct.PAGES['163fh'],
                     pageNo, start, end, _random(5))
    for _ in range(retry_count):
        time.sleep(pause)
        if pageNo>0:
                print rv.DP_MSG%pageNo
        try:
            with urlopen(url) as resp:
                lines = resp.read()
                lines = lines.replace('--', '0')
                lines = json.loads(lines)
                data = lines['list']
                df = pd.DataFrame(data)
                df = df.drop(['CODE', 'ESYMBOL', 'EXCHANGE', 'NAME', 'RN', 'SHANGQIGUSHU',
                              'SHANGQISHIZHI', 'SHANGQISHULIANG'], axis=1)
                for col in ['GUSHU', 'GUSHUBIJIAO', 'SHIZHI', 'SCSTC27']:
                    df[col] = df[col].astype(float)
                df['SCSTC27'] = df['SCSTC27']*100
                df['GUSHU'] = df['GUSHU']/10000
                df['GUSHUBIJIAO'] = df['GUSHUBIJIAO']/10000
                df['SHIZHI'] = df['SHIZHI']/10000
                df['GUSHU'] = df['GUSHU'].map(ct.FORMAT)
                df['GUSHUBIJIAO'] = df['GUSHUBIJIAO'].map(ct.FORMAT)
                df['SHIZHI'] = df['SHIZHI'].map(ct.FORMAT)
                df['SCSTC27'] = df['SCSTC27'].map(ct.FORMAT)
                df.columns = rv.FUND_HOLDS_COLS
                df = df[['code', 'name', 'date', 'nums', 'nlast', 'count', 
                         'clast', 'amount', 'ratio']]
        except _network_error_classes:
            pass
        else:
            if pageNo == 0:
                return df, int(lines['pagecount'])
            else:
                return df
    raise IOError("获取失败，请检查网络和URL:%s" % url)    
    

def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))  

    
def _check_input(year, quarter):
    if type(year) is str or year < 1989 :
        raise TypeError('年度输入错误：请输入1989年以后的年份数字，格式：YYYY')
    elif quarter is None or type(quarter) is str or quarter not in [1, 2, 3, 4]:
        raise TypeError('季度输入错误：请输入1、2、3或4数字')
    else:
        return True    
