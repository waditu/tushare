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
import urllib2
import json
import re
from pandas.util.testing import _network_error_classes
import time
import tushare.stock.fundamental as fd


def get_industry_classifyed():
    """
        获取行业分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :行业名称
    """
    df = _get_type_data(ct.SINA_INDUSTRY_INDEX_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], ct.PAGES['ids']))
    data = []
    for row in df.values:
        rowDf =  _get_detail(row[0])
        rowDf['c_name'] = row[1]
        data.append(rowDf)
    data = pd.concat(data,ignore_index=True)
    return data
        

def get_concept_classifyed():
    """
        获取概念分类数据
    Return
    --------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :概念名称
    """
    df = _get_type_data(ct.SINA_CONCEPTS_INDEX_URL%(ct.P_TYPE['http'], ct.DOMAINS['sf'], ct.PAGES['cpt']))
    data = []
    for row in df.values:
        rowDf =  _get_detail(row[0])
        rowDf['c_name'] = row[1]
        data.append(rowDf)
    data = pd.concat(data,ignore_index=True)
    return data


def get_area_classifyed(file_path=None):
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
    df = df[['name','area']]
    df.reset_index(level=0, inplace=True)
    df = df.sort('area').reset_index(drop=True)
    return df


def get_gem_classifyed(file_path=None):
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
    df = df[['code','name']]
    df = df.ix[df.code.str[0] == '3']
    df = df.sort('code').reset_index(drop=True)
    return df
    

def get_sme_classifyed(file_path=None):
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
    df = df[['code','name']]
    df = df.ix[df.code.str[0:3] == '002']
    df = df.sort('code').reset_index(drop=True)
    return df 

def get_st_classifyed(file_path=None):
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
    df = df[['code','name']]
    df = df.ix[df.name.str.contains('ST')]
    df = df.sort('code').reset_index(drop=True)
    return df 


def _get_detail(tag,retry_count=3,pause=0.001):
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            print 'getting tag : %s'%tag
            request = urllib2.Request(ct.SINA_DATA_DETAIL_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],ct.PAGES['jv'],tag))
            text = urllib2.urlopen(request,timeout=10).read()
        except _network_error_classes:
            pass
        else:
            reg = re.compile(r'\,(.*?)\:') 
            text = reg.sub(r',"\1":', text) 
            text = text.replace('"{symbol','{"symbol')
            text = text.replace('{symbol','{"symbol"')
            jstr = json.dumps(text,encoding='GBK')
            js = json.loads(jstr)
            the_fields = ['code','symbol','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio']
            df = pd.DataFrame(pd.read_json(js,dtype={'code':object}),columns=the_fields)
            df = df[['code','name']]
            return df
        raise IOError("%s获取失败，请检查网络和URL:%s" % (code, url))
    

def _get_type_data(url):
    try:
        request = urllib2.Request(url)
        data_str = urllib2.urlopen(request, timeout=10).read()
        data_str = data_str.decode('GBK')
        data_str = data_str.split('=')[1]
        data_json = json.loads(data_str)
        df = pd.DataFrame([[row.split(',')[0],row.split(',')[1]] for row in data_json.values()], columns=['tag', 'name'])
        return df
    except Exception as er:
        print str(er)

