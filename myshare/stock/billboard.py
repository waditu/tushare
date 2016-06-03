#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
龙虎榜数据
Created on 2015年6月10日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import pandas
from pandas.compat import StringIO
from io import BytesIO
import constants
import numpy
import time
import json
import re
import lxml.html
from lxml import etree
from myshare.util import date_helper
from enum import Enum
import ref_vars


try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


LhbPeriod = Enum('LhbPeriod', (('five', 5), ('ten', 10), ('thirty', 30), ('sixty', 60)))


def top_list(date=None, retry_count=3, pause=0.001):
    """
    获取每日龙虎榜列表
    Parameters
    --------
    date:string
                明细数据日期 format：YYYY-MM-DD 如果为空，返回最近一个交易日的数据
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    Return
    ------
    DataFrame
        code：代码
        name ：名称
        pchange：涨跌幅
        amount：龙虎榜成交额(万)
        buy：买入额(万)
        bratio：占总成交比例
        sell：卖出额(万)
        sratio ：占总成交比例
        reason：上榜原因
        date  ：日期
    """
    if date is None:
        if date_helper.get_hour() < 18:
            date = date_helper.last_trade_date()
        else:
            date = date_helper.today()
    elif date_helper.is_holiday(date):
        return None

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            url = constants.LHB_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['east'], date, date)
            lhb_data = lhb_info(url)
            data_frame = pandas.DataFrame(lhb_data, columns=constants.LHB_EAST_COLS)
            data_frame.columns = constants.LHB_COLS
            data_frame['buy'] = data_frame['buy'].astype(float)
            data_frame['sell'] = data_frame['sell'].astype(float)
            data_frame['amount'] = data_frame['amount'].astype(float)
            data_frame['turnover'] = data_frame['turnover'].astype(float)
            data_frame['buy_ratio'] = data_frame['buy'] / data_frame['turnover']
            data_frame['sell_ratio'] = data_frame['sell'] / data_frame['turnover']
            data_frame['buy_ratio'] = data_frame['buy_ratio'].map(constants.two_decimal)
            data_frame['sell_ratio'] = data_frame['sell_ratio'].map(constants.two_decimal)
            data_frame['date'] = date
            for col in ['amount', 'buy', 'sell']:
                data_frame[col] = data_frame[col].astype(float) / 10000
                data_frame[col] = data_frame[col].map(constants.two_decimal)
            data_frame = data_frame.drop('turnover', 1)
            return data_frame
        except Exception as e:
            print(e)
        raise IOError(constants.NETWORK_URL_ERROR_MSG)


def cap_tops(period=LhbPeriod.five, retry_count=3, pause=0.001):
    """
    获取个股上榜统计数据
    Parameters
    --------
        period:int
                  周期，统计n天以来上榜次数，默认为5天，其余是10、30、60
        retry_count : int, 默认 3
                     如遇网络等问题重复执行的次数
        pause : int, 默认 0
                    重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ------
    DataFrame
        code：代码
        name：名称
        count：上榜次数
        bamount：累积购买额(万)
        samount：累积卖出额(万)
        net：净额(万)
        bcount：买入席位数
        scount：卖出席位数
    """

    if isinstance(period, LhbPeriod):
        constants.console_write(constants.DATA_GETTING_TIPS)
        df = _cap_tops(days, page_no=1, retry_count=retry_count,
                       pause=pause)
        df['code'] = df['code'].map(lambda x: str(x).zfill(6))
        if df is not None:
            df = df.drop_duplicates('code')
        return df
    else:
        TypeError(constants.LHB_MSG)


# def is_lhb_period(period):
#     return is




# def request_html(url, encoding='GBK'):
#     return request(url).decode(encoding)


def lhb_info(url):
    # print(url)
    html = request(url)
    regex = re.compile('\[.*\]')
    # regex = re.compile('\{.*\}')
    json_content = regex.search(html).group(0)
    stock_info = json.loads(json_content)
    # print(stock_info)
    return stock_info

lhb_url = 'http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/' \
      'pagesize=200,page=1,sortRule=-1,sortType=,' \
      'startDate=2016-05-12,endDate=2016-05-12,gpfw=0,js=vardata_tab_1.html'
result = request(lhb_url)


def stock_tops(period=LhbPeriod.five, retry_count=3, pause=0.001):
    """
    获取个股上榜统计数据
    Parameters
    --------
        period:int
                  天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
        retry_count : int, 默认 3
                     如遇网络等问题重复执行的次数
        pause : int, 默认 0
                    重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ------
    DataFrame
        code：代码
        name：名称
        count：上榜次数
        bamount：累积购买额(万)
        samount：累积卖出额(万)
        net：净额(万)
        bcount：买入席位数
        scount：卖出席位数
    """

    # if constants._check_lhb_input(days) is True:
    if period is True:
        constants.console_write(constants.DATA_GETTING_TIPS)
        data_frame = _cap_tops(period, page_no=1, retry_count=retry_count,
                               pause=pause)
        data_frame['code'] = data_frame['code'].map(lambda x: str(x).zfill(6))
        if data_frame is not None:
            data_frame = data_frame.drop_duplicates('code')
        return data_frame


def _cap_tops(period=5, page_no=1, retry_count=3, pause=0.001, data_arr=pandas.DataFrame()):
    constants.console_write(constants.DATA_GETTING_FLAG)

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            # request = Request(constants.LHB_SINA_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['vsf'], rv.LHB_KINDS[0],
            #                                             constants.PAGES['fd'], period, page_no))
            # text = urlopen(request, timeout=10).read()
            # text = text.decode('GBK')

            url = constants.LHB_SINA_URL_GG % (period, page_no)
            response = request(url)
            doc = lxml.html.document_fromstring(response)
            nodes = doc.xpath(r'//table[@id="dataTable"]/tr')
            print(nodes)
            lhb_data = [etree.tostring(node).decode('utf-8') for node in nodes]

            # for node in nodes:
            #     print(node)

            lhb_data = ''.join(lhb_data)
            lhb_data = '<table>%s</table>' % lhb_data
            data_frame = pandas.read_html(lhb_data)[0]
            data_frame.columns = constants.LHB_GGTJ_COLS
            data_arr = data_arr.append(data_frame, ignore_index=True)
            pages = doc.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')

            print(pages)

            if len(pages)>0:
                page_no = re.findall(r'\d+', pages[0])[0]
                return _cap_tops(period, page_no, retry_count, pause, data_arr)
            else:
                return data_arr
        except Exception as e:
            print(e)


def stock_tops_page(period=5, page_no=1):
    constants.console_write(constants.DATA_GETTING_FLAG)
    try:
        url = constants.LHB_SINA_URL_GG % (period, page_no)
        html = request(url)
        # regex = re.search('<table>(<tr>.*</tr>)</table>', html)
        match_object = re.search('table', html)
        print(match_object)
        # doc = lxml.html.document_fromstring(response)
        # nodes = doc.xpath(r'//table[@id="dataTable"]/tr')
        # print(nodes)
        # lhb_data = [etree.tostring(node).decode('utf-8') for node in nodes]

        # for node in nodes:
        #     print(node)

        # lhb_data = ''.join(lhb_data)
        lhb_data = '<table>%s</table>' % lhb_data
        print(lhb_data)
        # data_frame = pandas.read_html(lhb_data)[0]
        # data_frame.columns = constants.LHB_GGTJ_COLS
        # print(data_frame)
        # data_arr = data_arr.append(data_frame, ignore_index=True)
        # pages = doc.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
    except Exception as e:
        print(e)


def _cap_tops(period=5, page_no=1, retry_count=3, pause=0.001, data_arr=pandas.DataFrame()):
    constants.console_write(constants.DATA_GETTING_FLAG)

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            # request = Request(constants.LHB_SINA_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['vsf'], rv.LHB_KINDS[0],
            #                                             constants.PAGES['fd'], period, page_no))
            # text = urlopen(request, timeout=10).read()
            # text = text.decode('GBK')

            url = constants.LHB_SINA_URL_GG % (period, page_no)
            response = request(url)
            tree = lxml.html.document_fromstring(response)
            nodes = tree.xpath(r'//table[@id="dataTable"]/tr')
            print(nodes)
            sarr = [etree.tostring(node).decode('utf-8') for node in nodes]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            data_frame = pandas.read_html(sarr)[0]
            data_frame.columns = constants.LHB_GGTJ_COLS
            data_arr = data_arr.append(data_frame, ignore_index=True)
            nextPage = nodes.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')

            if len(nextPage)>0:
                page_no = re.findall(r'\d+', nextPage[0])[0]
                return _cap_tops(period, page_no, retry_count, pause, data_arr)
            else:
                return data_arr
        except Exception as e:
            print(e)


def broker_tops(days=5, retry_count=3, pause=0.001):
    """
    获取营业部上榜统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ---------
    broker：营业部名称
    count：上榜次数
    bamount：累积购买额(万)
    bcount：买入席位数
    samount：累积卖出额(万)
    scount：卖出席位数
    top3：买入前三股票
    """
    if constants._check_lhb_input(days) is True:
        constants._write_head()
        data_frame =  _broker_tops(days, pageNo=1, retry_count=retry_count,
                        pause=pause)
        return data_frame


def _broker_tops(last=5, pageNo=1, retry_count=3, pause=0.001, dataArr=pandas.DataFrame()):
    constants._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['vsf'], rv.LHB_KINDS[1],
                                               constants.PAGES['fd'], last, pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if constants.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            data_frame = pandas.read_html(sarr)[0]
            data_frame.columns = rv.LHB_YYTJ_COLS
            dataArr = dataArr.append(data_frame, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage)>0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _broker_tops(last, pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def inst_tops(days= 5, retry_count= 3, pause= 0.001):
    """
    获取机构席位追踪统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    Return
    --------
    code:代码
    name:名称
    bamount:累积买入额(万)
    bcount:买入次数
    samount:累积卖出额(万)
    scount:卖出次数
    net:净额(万)
    """
    if constants._check_lhb_input(days) is True:
        constants._write_head()
        data_frame =  _inst_tops(days, pageNo=1, retry_count=retry_count,
                        pause=pause)
        data_frame['code'] = data_frame['code'].map(lambda x: str(x).zfill(6))
        return data_frame


def _inst_tops(last=5, pageNo=1, retry_count=3, pause=0.001, dataArr=pandas.DataFrame()):
    constants._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL%(constants.PROTOCOLS['http'], constants.DOMAINS['vsf'], rv.LHB_KINDS[2],
                                               constants.PAGES['fd'], last, pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if constants.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            data_frame = pandas.read_html(sarr)[0]
            data_frame = data_frame.drop([2,3], axis=1)
            data_frame.columns = rv.LHB_JGZZ_COLS
            dataArr = dataArr.append(data_frame, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage)>0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _inst_tops(last, pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def inst_detail(retry_count= 3, pause= 0.001):
    """
    获取最近一个交易日机构席位成交明细统计数据
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    Return
    ----------
    code:股票代码
    name:股票名称
    date:交易日期
    bamount:机构席位买入额(万)
    samount:机构席位卖出额(万)
    type:类型
    """
    constants._write_head()
    data_frame =  _inst_detail(pageNo=1, retry_count=retry_count,
                        pause=pause)
    if len(data_frame)>0:
        data_frame['code'] = data_frame['code'].map(lambda x: str(x).zfill(6))
    return data_frame


def _inst_detail(pageNo=1, retry_count=3, pause=0.001, dataArr=pandas.DataFrame()):
    constants._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL%(constants.PROTOCOLS['http'], constants.DOMAINS['vsf'], rv.LHB_KINDS[3],
                                               constants.PAGES['fd'], '', pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if constants.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            data_frame = pandas.read_html(sarr)[0]
            data_frame.columns = rv.LHB_JGMX_COLS
            dataArr = dataArr.append(data_frame, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage)>0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _inst_detail(pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def _f_rows(x):
    if '%' in x[3]:
        x[11] = x[6]
        for i in range(6, 11):
            x[i] = x[i-5]
        for i in range(1, 6):
            x[i] = numpy.NaN
    return x

