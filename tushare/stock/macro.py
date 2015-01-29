# -*- coding:utf-8 -*- 

"""
宏观经济数据接口 
Created on 2015/01/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import macro_vars as vs
import pandas as pd
import numpy as np
import urllib2
import re
import json

def get_gdp_year():
    """
        获取年度国内生产总值数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp :国内生产总值(亿元)
        pc_gdp :人均国内生产总值(元)
        gnp :国民生产总值(亿元)
        pi :第一产业(亿元)
        si :第二产业(亿元)
        industry :工业(亿元)
        cons_industry :建筑业(亿元)
        ti :第三产业(亿元)
        trans_industry :交通运输仓储邮电通信业(亿元)
        lbdy :批发零售贸易及餐饮业(亿元)
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[0],0,70,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
    datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.GDP_YEAR_COLS)
    df[df==0] = np.NaN
    return df
    
def get_gdp_quarter():
    """
        获取季度国内生产总值数据
    Return
    --------
    DataFrame
        quarter :季度
        gdp :国内生产总值(亿元)
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业增加值(亿元)
        pi_yoy:第一产业增加值同比增长(%)
        si :第二产业增加值(亿元)
        si_yoy :第二产业增加值同比增长(%)
        ti :第三产业增加值(亿元)
        ti_yoy :第三产业增加值同比增长(%)
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[0],1,250,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
    datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.GDP_QUARTER_COLS)
    df['quarter'] = df['quarter'].astype(object)
    df[df==0] = np.NaN
    return df


def get_gdp_for():
    """
        获取三大需求对GDP贡献数据
    Return
    --------
    DataFrame
        year :统计年度
        end_for :最终消费支出贡献率(%)
        for_rate :最终消费支出拉动(百分点)
        asset_for :资本形成总额贡献率(%)
        asset_rate:资本形成总额拉动(百分点)
        goods_for :货物和服务净出口贡献率(%)
        goods_rate :货物和服务净出口拉动(百分点)
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[0],4,80,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
    datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.GDP_FOR_COLS)
    df[df==0] = np.NaN
    return df

def get_gdp_pull():
    """
        获取三大产业对GDP拉动数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业拉动率(%)
        si :第二产业拉动率(%)
        industry:其中工业拉动(%)
        ti :第三产业拉动率(%)
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[0],5,60,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
    datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.GDP_PULL_COLS)
    df[df==0] = np.NaN
    return df

def get_gdp_contrib():
    """
        获取三大产业贡献率数据
    Return
    --------
    DataFrame
        year :统计年度
        gdp_yoy :国内生产总值
        pi :第一产业献率(%)
        si :第二产业献率(%)
        industry:其中工业献率(%)
        ti :第三产业献率(%)
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[0],6,60,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
    datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.GDP_CONTRIB_COLS)
    df[df==0] = np.NaN
    return df

def get_cpi():
    """
        获取居民消费价格指数数据
    Return
    --------
    DataFrame
        month :统计月份
        cpi :价格指数
    """
    rdint = vs.random()
    url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[1],0,600,rdint)
    request = urllib2.Request(url)
    text = urllib2.urlopen(request,timeout=10).read()

    regSym = re.compile(r'\,count:(.*?)\}')
    datastr = regSym.findall(text)
    datastr = datastr[0]
    datastr = datastr.split('data:')[1]
#     datastr = datastr.replace('"','').replace('null','0')
    js = json.loads(datastr)
    df = pd.DataFrame(js,columns=vs.CPI_COLS)
    df['cpi'] = df['cpi'].astype(float)
    return df

# def get_ppi():
#     """
#         获取工业品出厂价格指数数据
#     Return
#     --------
#     DataFrame
#         month :统计月份
#         ppi :价格指数
#     """
#     rdint = vs.random()
#     url = vs.MACRO_URL%(vs.P_TYPE['http'],vs.DOMAINS['sina'],rdint,vs.MACRO_TYPE[1],0,600,rdint)
#     request = urllib2.Request(url)
#     text = urllib2.urlopen(request,timeout=10).read()
# 
#     regSym = re.compile(r'\,count:(.*?)\}')
#     datastr = regSym.findall(text)
#     datastr = datastr[0]
#     datastr = datastr.split('data:')[1]
# #     datastr = datastr.replace('"','').replace('null','0')
#     js = json.loads(datastr)
#     df = pd.DataFrame(js,columns=vs.CPI_COLS)
#     df['value'] = df['value'].astype(float)
#     return df

if __name__ == '__main__':
    print get_gdp_quarter()

