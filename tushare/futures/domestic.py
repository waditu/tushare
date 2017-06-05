#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年06月04日
@author: debugo
@contact: me@debugo.com
'''

import json
from urllib import request, error
from urllib.parse import urlencode
from datetime import date, timedelta
from bs4 import BeautifulSoup
import pandas as pd
from tushare.future import domestic_cons as ct

def get_cffex_daily(day=None):
    """
        获取中金所日交易数据
    Parameters
    ------
        day: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            中金所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_close     前收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """
    day = ct.convert_date(day) if day is not None else date.today()
    try:
        html = request.urlopen(request.Request(ct.CFFEX_DAILY_URL % (day.strftime('%Y%m'), day.strftime('%d'), day.strftime('%Y%m%d')), headers=ct.SIM_HAEDERS)).read().decode('gbk','ignore')
    except error.HTTPError as reason:
        if reason.code != 404:
            print(ct.CFFEX_DAILY_URL % (day.strftime('%Y%m'), day.strftime('%d'), day.strftime('%Y%m%d')), reason)
        return

    if html.find(u'网页错误') >= 0:
        return
    html = [i.replace(' ','').split(',') for i in html.split('\n')[:-2] if i[0][0] != u'小' ]
    
    if html[0][0]!=u'合约代码':
        return
    
    dict_data = list()
    day_const = day.strftime('%Y%m%d')
    for row in html[1:]:
        m = ct.FUTURE_SYMBOL_PATTERN.match(row[0])
        if not m:
            continue
        row_dict = {'date': day_const, 'symbol': row[0], 'variety': m.group(1)}
        
        for i,field in enumerate(ct.CFFEX_COLUMNS):
            if row[i+1] == u"":
                row_dict[field] = 0.0
            else:
                row_dict[field] = float(row[i+1])
        row_dict[ct.OUTPUT_COLUMNS[ct.PRE_SETTLE_LOC]] = row_dict[ct.OUTPUT_COLUMNS[ct.CLOSE_LOC]] - row_dict['change1']
        row_dict[ct.OUTPUT_COLUMNS[ct.PRE_CLOSE_LOC]] = row_dict[ct.OUTPUT_COLUMNS[ct.CLOSE_LOC]] - row_dict['change2']
        dict_data.append(row_dict)
        
    return pd.DataFrame(dict_data)[ct.OUTPUT_COLUMNS]


def get_czce_daily(day=None):
    """
        获取郑商所日交易数据
    Parameters
    ------
        day: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            郑商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_close     前收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """
    day = ct.convert_date(day) if day is not None else date.today()

    try:
        html = request.urlopen(request.Request(ct.CZCE_DAILY_URL % (day.strftime('%Y'),day.strftime('%Y%m%d')), headers=ct.SIM_HAEDERS)).read().decode('gbk','ignore')
    except error.HTTPError as reason:
        if reason.code != 404:
            print(ct.CZCE_DAILY_URL % (day.strftime('%Y'),day.strftime('%Y%m%d')), reason)            
        return
    
    if html.find('您的访问出错了') >= 0:
        return
    html = [i.replace(' ','').split('|') for i in html.split('\n')[:-4] if i[0][0] != '小']
    if html[1][0]!='品种月份':
            return
    
    dict_data = list()
    day_const = int(day.strftime('%Y%m%d'))
    for ihtml in html[2:]:
        m = ct.FUTURE_SYMBOL_PATTERN.match(ihtml[0])
        if not m:
            continue
        row_dict = {'date': day_const, 'symbol': ihtml[0], 'variety': m.group(1)}
        
        for i,field in enumerate(ct.CZCE_COLUMNS):
            if ihtml[i+1] == "\r":
                row_dict[field] = 0.0
            else:
                ihtml[i+1] = ihtml[i+1].replace(',','')
                row_dict[field] = float(ihtml[i+1])
        row_dict['pre_settle'] = row_dict['close'] - row_dict['change2']
        dict_data.append(row_dict)

    return pd.DataFrame(dict_data)[ct.OUTPUT_COLUMNS]


def get_shfe_vwap(day):
    """
        获取上期所日成交均价数据
    Parameters
    ------
        day: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            郑商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                time_range    vwap时段，分09:00-10:15和09:00-15:00两类
                vwap          加权平均成交均价
        或 None(给定日期没有数据)
    """    
    day = ct.convert_date(day) if day is not None else date.today()

    try:
        json_data = json.loads(request.urlopen(request.Request(ct.SHFE_VWAP_URL % (day.strftime('%Y%m%d')), headers=ct.SIM_HAEDERS)).read().decode('utf8'))
    except error.HTTPError as reason:
        if reason.code != 404:
            print(ct.SHFE_DAILY_URL % (day.strftime('%Y%m%d')), reason)            
        return    

    if len(json_data['o_currefprice']) == 0:
        return
    
    df = pd.DataFrame(json_data['o_currefprice'])
    df['INSTRUMENTID'] = df['INSTRUMENTID'].str.strip()
    df[':B1'].astype('int16')
    return df.rename(columns=ct.SHFE_VWAP_COLUMNS)[list(ct.SHFE_VWAP_COLUMNS.values())]    


def get_shfe_daily(day=None):
    """
        获取上期所日交易数据
    Parameters
    ------
        day: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            上期所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_close     前收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """    
    day = ct.convert_date(day) if day is not None else date.today()

    try:
        json_data = json.loads(request.urlopen(request.Request(ct.SHFE_DAILY_URL % (day.strftime('%Y%m%d')), headers=ct.SIM_HAEDERS)).read().decode('utf8'))
    except error.HTTPError as reason:
        if reason.code != 404:
            print(ct.SHFE_DAILY_URL % (day.strftime('%Y%m%d')), reason)            
        return    

    if len(json_data['o_curinstrument']) == 0:
        return
    
    df = pd.DataFrame([row for row in json_data['o_curinstrument'] if row['DELIVERYMONTH'] != '小计' and row['DELIVERYMONTH'] != ''])
    df['variety'] = df.PRODUCTID.str.slice(0, -6)
    df['symbol'] = df['variety'].str.upper() + df['DELIVERYMONTH']
    df['date'] = day.strftime('%Y%m%d')
    vwap_df = get_shfe_vwap(day)
    if vwap_df is not None:
        df = pd.merge(df, vwap_df[vwap_df.time_range == '9:00-15:00'], on=['date', 'symbol'], how='left')
    else:
        print('Failed to fetch SHFE vwap.')
    df.rename(columns=ct.SHFE_COLUMNS, inplace=True)
    df['turnover'] = df.vwap * df.volume    
    df['pre_close'] = df['ZD2_CHG'] + df['close']
    return df[ct.OUTPUT_COLUMNS]


def get_dce_daily(day=None):
    """
        获取大连商品交易所日交易数据
    Parameters
    ------
        day: 日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
    Return
    -------
        DataFrame
            大商所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_close     前收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """    
    day = ct.convert_date(day) if day is not None else date.today()    
    
    url = ct.DCE_DAILY_URL + '?' + urlencode({"currDate":day.strftime('%Y%m%d'),"year":day.strftime('%Y'), "month": str(int(day.strftime('%m'))-1), "day":day.strftime('%d')})
    response = request.urlopen(request.Request(url, method='POST', headers=ct.DCE_HEADERS)).read().decode('utf8')
    if u'错误：您所请求的网址（URL）无法获取' in response:
        return
    elif u'暂无数据' in response:
        return
    
    data = BeautifulSoup(response, 'html.parser').find_all('tr')
    if len(data) == 0:
        return
    
    dict_data = list()
    for idata in data[1:]:
        if '小计' in idata.text or '总计' in idata.text:
            continue
        x = idata.find_all('td')
        row_dict = dict()
        for i,field in enumerate(ct.DCE_COLUMNS):
            if i==0:
                row_dict[field] = ct.DCE_MAP[x[i].text.strip()]
            elif i>=2:
                if '-' in x[i].text.strip():
                    row_dict[field] = 0.0                
                else:
                    row_dict[field] = float(x[i].text.strip().replace(',',''))
            else:
                row_dict[field] = x[i].text.strip()
        dict_data.append(row_dict)
    df = pd.DataFrame(dict_data)
    df['date'] = day.strftime('%Y%m%d')
    df['pre_close'] = df.close - df.change1
    df['symbol'] = df.variety + df.month
    return df[ct.OUTPUT_COLUMNS]


def get_future_daily(start=None, end=None, market='CFFEX'):
    """
        获取中金所日交易数据
    Parameters
    ------
        start: 开始日期 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        end: 结束数据 format：YYYY-MM-DD 或 YYYYMMDD 或 datetime.date对象 为空时为当天
        market: 'CFFEX' 中金所, 'CZCE' 郑商所,  'SHFE' 上期所, 'DCE' 大商所 之一。默认为中金所 
    Return
    -------
        DataFrame
            中金所日交易数据(DataFrame):
                symbol        合约代码
                date          日期
                open          开盘价
                high          最高价
                low           最低价
                close         收盘价
                pre_close     前收盘价
                volume        成交量
                open_interest 持仓量
                turnover      成交额
                settle        结算价
                pre_settle    前结算价
                variety       合约类别
        或 None(给定日期没有交易数据)
    """
    if market.upper() == 'CFFEX':
        f = get_cffex_daily
    elif market.upper() == 'CZCE':
        f = get_czce_daily
    elif market.upper() == 'SHFE':
        f = get_shfe_daily
    elif market.upper() == 'DCE':
        f = get_dce_daily
    else:
        print('Invalid market.')
        return
    
    start = ct.convert_date(start) if start is not None else date.today()
    end = ct.convert_date(end) if end is not None else date.today()


    df_list = list()
    while start <= end:
        df = f(start)
        if df is not None:
            df_list.append(df)
        start += timedelta(days=1)

    if len(df_list) > 0:
        return pd.concat(df_list)
