# -*- coding:utf-8 -*-

"""
获取股票分类数据接口 
Created on 2015/02/01
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import pandas as pd
from tushare.stock import cons as ct
import json
import re
from pandas.util.testing import _network_error_classes
import time
import tushare.stock.fundamental as fd
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def get_industry_classified():
    """
        获取行业分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :行业名称
    """
    df = _get_type_data(ct.SINA_INDUSTRY_INDEX_URL%(ct.P_TYPE['http'],
                                                    ct.DOMAINS['vsf'], ct.PAGES['ids']))
    data = []
    ct._write_head()
    for row in df.values:
        rowDf =  _get_detail(row[0])
        rowDf['c_name'] = row[1]
        data.append(rowDf)
    data = pd.concat(data, ignore_index=True)
    return data
        

def get_concept_classified():
    """
        获取概念分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :概念名称
    """
    ct._write_head()
    df = _get_type_data(ct.SINA_CONCEPTS_INDEX_URL%(ct.P_TYPE['http'],
                                                    ct.DOMAINS['sf'], ct.PAGES['cpt']))
    data = []
    for row in df.values:
        rowDf =  _get_detail(row[0])
        rowDf['c_name'] = row[1]
        data.append(rowDf)
    data = pd.concat(data,ignore_index=True)
    return data


def get_area_classified(file_path=None):
    """
        获取地域分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        area :地域名称
    """
    df = fd.get_stock_basics(file_path)
    df = df[['name', 'area']]
    df.reset_index(level=0, inplace=True)
    df = df.sort('area').reset_index(drop=True)
    return df


def get_gem_classified(file_path=None):
    """
        获取创业板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    df = fd.get_stock_basics(file_path)
    df.reset_index(level=0, inplace=True)
    df = df[ct.FOR_CLASSIFY_B_COLS]
    df = df.ix[df.code.str[0] == '3']
    df = df.sort('code').reset_index(drop=True)
    return df
    

def get_sme_classified(file_path=None):
    """
        获取中小板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    df = fd.get_stock_basics(file_path)
    df.reset_index(level=0, inplace=True)
    df = df[ct.FOR_CLASSIFY_B_COLS]
    df = df.ix[df.code.str[0:3] == '002']
    df = df.sort('code').reset_index(drop=True)
    return df 

def get_st_classified(file_path=None):
    """
        获取风险警示板股票
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    df = fd.get_stock_basics(file_path)
    df.reset_index(level=0, inplace=True)
    df = df[ct.FOR_CLASSIFY_B_COLS]
    df = df.ix[df.name.str.contains('ST')]
    df = df.sort('code').reset_index(drop=True)
    return df 


def _get_detail(tag, retry_count=3, pause=0.001):
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            ct._write_console()
            request = Request(ct.SINA_DATA_DETAIL_URL%(ct.P_TYPE['http'],
                                                               ct.DOMAINS['vsf'], ct.PAGES['jv'],
                                                               tag))
            text = urlopen(request, timeout=10).read()
            text = text.decode('gbk')
        except _network_error_classes:
            pass
        else:
            reg = re.compile(r'\,(.*?)\:') 
            text = reg.sub(r',"\1":', text) 
            text = text.replace('"{symbol', '{"symbol')
            text = text.replace('{symbol', '{"symbol"')
            jstr = json.dumps(text)
            js = json.loads(jstr)
            df = pd.DataFrame(pd.read_json(js, dtype={'code':object}), columns=ct.THE_FIELDS)
            df = df[ct.FOR_CLASSIFY_B_COLS]
            return df
        raise IOError("数据获取失败，请检查网络和URL")
    

def _get_type_data(url):
    try:
        request = Request(url)
        data_str = urlopen(request, timeout=10).read()
        data_str = data_str.decode('GBK')
        data_str = data_str.split('=')[1]
        data_json = json.loads(data_str)
        df = pd.DataFrame([[row.split(',')[0], row.split(',')[1]] for row in data_json.values()],
                          columns=['tag', 'name'])
        return df
    except Exception as er:
        print(str(er))


def get_hs300s():
    """
    获取沪深300当前成份股及所占权重
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        date :日期
        weight:权重
    """
    try:
        df = pd.read_excel(ct.HS300_CLASSIFY_URL%(ct.P_TYPE['http'], ct.DOMAINS['idx'], 
                                                  ct.INDEX_C_COMM, ct.PAGES['hs300b']), parse_cols=[0,1])
        df.columns = ct.FOR_CLASSIFY_B_COLS
        df['code'] = df['code'].map(lambda x :str(x).zfill(6))
        wt = pd.read_excel(ct.HS300_CLASSIFY_URL%(ct.P_TYPE['http'], ct.DOMAINS['idx'], 
                                                  ct.INDEX_C_COMM, ct.PAGES['hs300w']), parse_cols=[0,3,6])
        wt.columns = ct.FOR_CLASSIFY_W_COLS
        wt['code'] = wt['code'].map(lambda x :str(x).zfill(6))
        return pd.merge(df,wt)
    except Exception as er:
        print(str(er))


def get_sz50s():
    """
    获取上证50成份股
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    try:
        df = pd.read_excel(ct.HS300_CLASSIFY_URL%(ct.P_TYPE['http'], ct.DOMAINS['idx'], 
                                                  ct.INDEX_C_COMM, ct.PAGES['sz50b']), parse_cols=[0,1])
        df.columns = ct.FOR_CLASSIFY_B_COLS
        df['code'] = df['code'].map(lambda x :str(x).zfill(6))
        return df
    except Exception as er:
        print(str(er))      


def get_zz500s():
    """
    获取中证500成份股
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
    """
    try:
        df = pd.read_excel(ct.HS300_CLASSIFY_URL%(ct.P_TYPE['http'], ct.DOMAINS['idx'], 
                                                  ct.INDEX_C_COMM, ct.PAGES['zz500b']), parse_cols=[0,1])
        df.columns = ct.FOR_CLASSIFY_B_COLS
        df['code'] = df['code'].map(lambda x :str(x).zfill(6))
        return df
    except Exception as er:
        print(str(er)) 

