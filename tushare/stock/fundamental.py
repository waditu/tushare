# -*- coding:utf-8 -*- 
"""
基本面数据接口 
Created on 2015/01/18
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
import pandas as pd
from tushare.stock import cons as ct
import urllib2


def get_stock_basics(file_path=ct.ALL_STOCK_BASICS_FILE):
    """
        获取个股基本情况
    Parameters
    --------
    file_path:a file path string,default as 'data/all.csv' in the package
        you can use your own file with the same columns 
    Return
    --------
        DataFrame
               code,代码
               name,名称
               industry,细分行业
               area,地区
               pe,市盈率
               outstanding,流通股本
               totals,总股本(万)
               totalAssets,总资产(万)
               liquidAssets,流动资产
               fixedAssets,固定资产
               reserved,公积金
               reservedPerShare,每股公积
               eps,每股收益
               bvps,每股净资
               pb,市净率
               timeToMarket,上市日期
    """
    df = pd.read_csv(file_path,dtype={'code':'object'},encoding='GBK')
    df = df.set_index('code')
    return df
    

if __name__ == '__main__':
    df = get_stock_basics()
    print df.count()

    