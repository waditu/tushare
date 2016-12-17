# -*- coding:utf-8 -*- 
"""
投资参考数据接口 
Created on 2015/03/21
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
from __future__ import division
from tushare.stock import cons as ct
from tushare.stock import ref_vars as rv
import pandas as pd
import time
import lxml.html
from lxml import etree
import re
import json
from pandas.compat import StringIO
from tushare.util import dateu as du
from tushare.util.netbase import Client
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def profit_data(year=2015, top=25, 
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
    
    if top == 'all':
        ct._write_head()
        df, pages = _dist_cotent(year, 0, retry_count, pause)
        for idx in range(1,int(pages)):
            df = df.append(_dist_cotent(year, idx, retry_count,
                                        pause), ignore_index=True)
        return df
    elif top <= 25:
        df, pages = _dist_cotent(year, 0, retry_count, pause)
        return df.head(top)
    else:
        if isinstance(top, int):
            ct._write_head()
            allPages = top/25+1 if top%25>0 else top/25
            df, pages = _dist_cotent(year, 0, retry_count, pause)
            if int(allPages) < int(pages):
                pages = allPages
            for idx in range(1, int(pages)):
                df = df.append(_dist_cotent(year, idx, retry_count,
                                            pause), ignore_index=True)
            return df.head(top)
        else:
            print(ct.TOP_PARAS_MSG)
    

def _fun_divi(x):
    if ct.PY3:
        reg = re.compile(r'分红(.*?)元', re.UNICODE)
        res = reg.findall(x)
        return 0 if len(res)<1 else float(res[0]) 
    else:
        if isinstance(x, unicode):
            s1 = unicode('分红','utf-8')
            s2 = unicode('元','utf-8')
            reg = re.compile(r'%s(.*?)%s'%(s1, s2), re.UNICODE)
            res = reg.findall(x)
            return 0 if len(res)<1 else float(res[0])
        else:
            return 0


def _fun_into(x):
    if ct.PY3:
            reg1 = re.compile(r'转增(.*?)股', re.UNICODE)
            reg2 = re.compile(r'送股(.*?)股', re.UNICODE)
            res1 = reg1.findall(x)
            res2 = reg2.findall(x)
            res1 = 0 if len(res1)<1 else float(res1[0])
            res2 = 0 if len(res2)<1 else float(res2[0])
            return res1 + res2
    else:
        if isinstance(x, unicode):
            s1 = unicode('转增','utf-8')
            s2 = unicode('送股','utf-8')
            s3 = unicode('股','utf-8')
            reg1 = re.compile(r'%s(.*?)%s'%(s1, s3), re.UNICODE)
            reg2 = re.compile(r'%s(.*?)%s'%(s2, s3), re.UNICODE)
            res1 = reg1.findall(x)
            res2 = reg2.findall(x)
            res1 = 0 if len(res1)<1 else float(res1[0])
            res2 = 0 if len(res2)<1 else float(res2[0])
            return res1 + res2
        else:
            return 0
    
    
def _dist_cotent(year, pageNo, retry_count, pause):
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            if pageNo > 0:
                ct._write_console()
            html = lxml.html.parse(rv.DP_163_URL%(ct.P_TYPE['http'], ct.DOMAINS['163'],
                     ct.PAGES['163dp'], year, pageNo))  
            res = html.xpath('//div[@class=\"fn_rp_list\"]/table')
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
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
            pages = []
            if pageNo == 0:
                page = html.xpath('//div[@class=\"mod_pages\"]/a')
                if len(page)>1:
                    asr = page[len(page)-2]
                    pages = asr.xpath('text()')
        except Exception as e:
            print(e)
        else:
            if pageNo == 0:
                return df, pages[0] if len(pages)>0 else 0
            else:
                return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)    


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
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        data =  _get_forecast_data(year, quarter, 1, pd.DataFrame())
        df = pd.DataFrame(data, columns=ct.FORECAST_COLS)
        df['code'] = df['code'].map(lambda x: str(x).zfill(6))
        return df


def _get_forecast_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        html = lxml.html.parse(ct.FORECAST_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], 
                                                ct.PAGES['fd'], year, quarter, pageNo,
                                                ct.PAGE_NUM[1]))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = sarr.replace('--', '0')
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df = df.drop([4, 5, 8], axis=1)
        df.columns = ct.FORECAST_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_forecast_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
            print(e)
    

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
    year = du.get_year() if year is None else year
    month = du.get_month() if month is None else month
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.XSG_URL%(ct.P_TYPE['http'], ct.DOMAINS['em'],
                                     ct.PAGES['emxsg'], year, month))
            lines = urlopen(request, timeout = 10).read()
            lines = lines.decode('utf-8') if ct.PY3 else lines
        except Exception as e:
            print(e)
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
    raise IOError(ct.NETWORK_URL_ERROR_MSG)   


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
    ct._write_head()
    df, pages = _holding_cotent(start, end, 0, retry_count, pause)
    for idx in range(1, pages):
        df = df.append(_holding_cotent(start, end, idx, retry_count, pause),
                  ignore_index=True)
    return df


def _holding_cotent(start, end, pageNo, retry_count, pause):
    for _ in range(retry_count):
        time.sleep(pause)
        if pageNo>0:
                ct._write_console()
        try:
            request = Request(rv.FUND_HOLDS_URL%(ct.P_TYPE['http'], ct.DOMAINS['163'],
                     ct.PAGES['163fh'], ct.PAGES['163fh'],
                     pageNo, start, end, _random(5)))
            lines = urlopen(request, timeout = 10).read()
            lines = lines.decode('utf-8') if ct.PY3 else lines
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
        except Exception as e:
            print(e)
        else:
            if pageNo == 0:
                return df, int(lines['pagecount'])
            else:
                return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)    
    

def new_stocks(retry_count=3, pause=0.001):
    """
    获取新股上市数据
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    code:股票代码
    name:名称
    ipo_date:上网发行日期
    issue_date:上市日期
    amount:发行数量(万股)
    markets:上网发行数量(万股)
    price:发行价格(元)
    pe:发行市盈率
    limit:个人申购上限(万股)
    funds：募集资金(亿元)
    ballot:网上中签率(%)
    """
    data = pd.DataFrame()
    ct._write_head()
    df = _newstocks(data, 1, retry_count,
                    pause)
    return df


def _newstocks(data, pageNo, retry_count, pause):
    for _ in range(retry_count):
        time.sleep(pause)
        ct._write_console()
        try:
            html = lxml.html.parse(rv.NEW_STOCKS_URL%(ct.P_TYPE['http'],ct.DOMAINS['vsf'],
                         ct.PAGES['newstock'], pageNo))
            res = html.xpath('//table[@id=\"NewStockTable\"]/tr')
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = sarr.replace('<font color="red">*</font>', '')
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(StringIO(sarr), skiprows=[0, 1])[0]
            df = df.drop([df.columns[idx] for idx in [1, 12, 13, 14]], axis=1)
            df.columns = rv.NEW_STOCKS_COLS
            df['code'] = df['code'].map(lambda x : str(x).zfill(6))
            res = html.xpath('//table[@class=\"table2\"]/tr[1]/td[1]/a/text()')
            tag = '下一页' if ct.PY3 else unicode('下一页', 'utf-8')
            hasNext = True if tag in res else False 
            data = data.append(df, ignore_index=True)
            pageNo += 1
            if hasNext:
                data = _newstocks(data, pageNo, retry_count, pause)
        except Exception as ex:
            print(ex)
        else:
            return data 


def sh_margins(start=None, end=None, retry_count=3, pause=0.001):
    """
    获取沪市融资融券数据列表
    Parameters
    --------
    start:string
                  开始日期 format：YYYY-MM-DD 为空时取去年今日
    end:string
                  结束日期 format：YYYY-MM-DD 为空时取当前日期
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rqyl: 本日融券余量
    rqylje: 本日融券余量金额(元)
    rqmcl: 本日融券卖出量
    rzrqjyzl:本日融资融券余额(元)
    """
    start = du.today_last_year() if start is None else start
    end = du.today() if end is None else end
    if du.diff_day(start, end) < 0:
        return None
    start, end = start.replace('-', ''), end.replace('-', '')
    data = pd.DataFrame()
    ct._write_head()
    df = _sh_hz(data, start=start, end=end,
                retry_count=retry_count,
                pause=pause)
    return df


def _sh_hz(data, start=None, end=None, 
           pageNo='', beginPage='',
           endPage='',
           retry_count=3, pause=0.001):
    for _ in range(retry_count):
        time.sleep(pause)
        ct._write_console()
        try:
            tail = rv.MAR_SH_HZ_TAIL_URL%(pageNo,
                                    beginPage, endPage)
            if pageNo == '':
                pageNo = 6
                tail = ''
            else:
                pageNo += 5
            beginPage = pageNo
            endPage = pageNo + 4
            url = rv.MAR_SH_HZ_URL%(ct.P_TYPE['http'], ct.DOMAINS['sseq'],
                                    ct.PAGES['qmd'], _random(5),
                                    start, end, tail,
                                    _random())
            ref = rv.MAR_SH_HZ_REF_URL%(ct.P_TYPE['http'], ct.DOMAINS['sse'])
            clt = Client(url, ref=ref, cookie=rv.MAR_SH_COOKIESTR)
            lines = clt.gvalue()
            lines = lines.decode('utf-8') if ct.PY3 else lines
            lines = lines[19:-1]
            lines = json.loads(lines)
            pagecount = int(lines['pageHelp'].get('pageCount'))
            datapage = int(pagecount/5+1 if pagecount%5>0 else pagecount/5)
            df = pd.DataFrame(lines['result'], columns=rv.MAR_SH_HZ_COLS)
            df['opDate'] = df['opDate'].map(lambda x: '%s-%s-%s'%(x[0:4], x[4:6], x[6:8]))
            data = data.append(df, ignore_index=True)
            if beginPage < datapage*5:
                data = _sh_hz(data, start=start, end=end, pageNo=pageNo, 
                       beginPage=beginPage, endPage=endPage, 
                       retry_count=retry_count, pause=pause)
        except Exception as e:
            print(e)
        else:
            return data
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def sh_margin_details(date='', symbol='', 
                      start='', end='',
                      retry_count=3, pause=0.001):
    """
    获取沪市融资融券明细列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 默认为空''
    symbol：string
                标的代码，6位数字e.g.600848，默认为空  
    start:string
                  开始日期 format：YYYY-MM-DD 默认为空''
    end:string
                  结束日期 format：YYYY-MM-DD 默认为空''
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rzche:本日融资偿还额(元)
    rqyl: 本日融券余量
    rqmcl: 本日融券卖出量
    rqchl: 本日融券偿还量
    """
    date = date if date == '' else date.replace('-', '')
    start = start if start == '' else start.replace('-', '')
    end = end if end == '' else end.replace('-', '')
    if (start != '') & (end != ''):
        date = ''
    data = pd.DataFrame()
    ct._write_head()
    df = _sh_mx(data, date=date, start=start,
                end=end, symbol=symbol,
                retry_count=retry_count,
                pause=pause)
    return df


def _sh_mx(data, date='', start='', end='', 
           symbol='',
           pageNo='', beginPage='',
           endPage='',
           retry_count=3, pause=0.001):
    for _ in range(retry_count):
        time.sleep(pause)
        ct._write_console()
        try:
            tail = '&pageHelp.pageNo=%s&pageHelp.beginPage=%s&pageHelp.endPage=%s'%(pageNo,
                                    beginPage, endPage)
            if pageNo == '':
                pageNo = 6
                tail = ''
            else:
                pageNo += 5
            beginPage = pageNo
            endPage = pageNo + 4
            ref = rv.MAR_SH_HZ_REF_URL%(ct.P_TYPE['http'], ct.DOMAINS['sse'])
            clt = Client(rv.MAR_SH_MX_URL%(ct.P_TYPE['http'], ct.DOMAINS['sseq'],
                                    ct.PAGES['qmd'], _random(5), date, 
                                    symbol, start, end, tail,
                                    _random()), ref=ref, cookie=rv.MAR_SH_COOKIESTR)
            lines = clt.gvalue()
            lines = lines.decode('utf-8') if ct.PY3 else lines
            lines = lines[19:-1]
            lines = json.loads(lines)
            pagecount = int(lines['pageHelp'].get('pageCount'))
            datapage = int(pagecount/5+1 if pagecount%5>0 else pagecount/5)
            if pagecount == 0:
                return data
            if pageNo == 6:
                ct._write_tips(lines['pageHelp'].get('total'))
            df = pd.DataFrame(lines['result'], columns=rv.MAR_SH_MX_COLS)
            df['opDate'] = df['opDate'].map(lambda x: '%s-%s-%s'%(x[0:4], x[4:6], x[6:8]))
            data = data.append(df, ignore_index=True)
            if beginPage < datapage*5:
                data = _sh_mx(data, start=start, end=end, pageNo=pageNo, 
                       beginPage=beginPage, endPage=endPage, 
                       retry_count=retry_count, pause=pause)
        except Exception as e:
            print(e)
        else:
            return data
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def sz_margins(start=None, end=None, retry_count=3, pause=0.001):
    """
    获取深市融资融券数据列表
    Parameters
    --------
    start:string
                  开始日期 format：YYYY-MM-DD 默认为上一周的今天
    end:string
                  结束日期 format：YYYY-MM-DD 默认为今日
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期(index)
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)
    """
    data = pd.DataFrame()
    if start is None and end is None:
        end = du.today()
        start = du.day_last_week()
    if start is None or end is None:
        ct._write_msg(rv.MAR_SZ_HZ_MSG2)
        return None
    try:
        date_range = pd.date_range(start=start, end=end, freq='B')
        if len(date_range)>261:
            ct._write_msg(rv.MAR_SZ_HZ_MSG)
        else:
            ct._write_head()
            for date in date_range:
                data = data.append(_sz_hz(str(date.date()), retry_count, pause) )
    except:
        ct._write_msg(ct.DATA_INPUT_ERROR_MSG)
    else:
        return data
        

def _sz_hz(date='', retry_count=3, pause=0.001):
    for _ in range(retry_count):
        time.sleep(pause)
        ct._write_console()
        try:
            request = Request(rv.MAR_SZ_HZ_URL%(ct.P_TYPE['http'], ct.DOMAINS['szse'],
                                    ct.PAGES['szsefc'], date))
            lines = urlopen(request, timeout = 10).read()
            if len(lines) <= 200:
                return pd.DataFrame()
            df = pd.read_html(lines, skiprows=[0])[0]
            df.columns = rv.MAR_SZ_HZ_COLS
            df['opDate'] = date
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def sz_margin_details(date='', retry_count=3, pause=0.001):
    """
    获取深市融资融券明细列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 默认为空''
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    
    Return
    ------
    DataFrame
    opDate:信用交易日期
    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)
    """
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.MAR_SZ_MX_URL%(ct.P_TYPE['http'], ct.DOMAINS['szse'],
                                    ct.PAGES['szsefc'], date))
            lines = urlopen(request, timeout = 10).read()
            if len(lines) <= 200:
                return pd.DataFrame()
            df = pd.read_html(lines, skiprows=[0])[0]
            df.columns = rv.MAR_SZ_MX_COLS
            df['stockCode'] = df['stockCode'].map(lambda x:str(x).zfill(6))
            df['opDate'] = date
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def top10_holders(code=None, year=None, quarter=None, gdtype='0',
                  retry_count=3, pause=0.001):
    if code is None:
        return None
    else:
        code = ct._code_to_symbol(code)
    gdtype = 'LT' if gdtype == '1' else ''
    qdate = ''
    if (year is not None) & (quarter is not None):
        qdate = du.get_q_date(year, quarter)
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.TOP10_HOLDERS_URL%(ct.P_TYPE['http'], ct.DOMAINS['gw'],
                                    gdtype, code.upper()))
            lines = urlopen(request, timeout = 10).read()
            lines = lines.decode('utf8') if ct.PY3 else lines
            reg = re.compile(r'= \'\[(.*?)\]\';')
            lines = reg.findall(lines)[0]
            jss = json.loads('[%s]' %lines)
            summ = []
            data = pd.DataFrame()
            for row in jss:
                qt = row['jzrq']
                hold = row['ljcy']
                change = row['ljbh']
                props = row['ljzb']
                arow = [qt, hold, change ,props]
                summ.append(arow)
                ls = row['sdgdList']
                dlist = []
                for inrow in ls:
                    sharetype = inrow['gbxz']
                    name = inrow['gdmc']
                    hold = inrow['cgs']
                    h_pro = inrow['zzgs']
                    status = inrow['zjqk']
                    dlist.append([qt, name, hold, h_pro, sharetype, status])
                ddata = pd.DataFrame(dlist, columns=rv.TOP10_PER_COLS)
                data = data.append(ddata, ignore_index=True)
            df = pd.DataFrame(summ, columns=rv.TOP10_SUMM_COLS)
            if qdate != '':
                df = df[df.quarter == qdate]
                data = data[data.quarter == qdate]
        except Exception as e:
            print(e)
        else:
            return df, data
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))
