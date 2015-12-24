# -*- coding:utf-8 -*- 
"""
电影票房 
Created on 2015/12/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
import pandas as pd
from tushare.stock import cons as ct
from tushare.util import dateu as du
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import time
import json

def realtime_boxoffice(retry_count=3,pause=0.001):
    """
    获取实时电影票房数据
    数据来源：EBOT艺恩票房智库
    Parameters
    ------
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 
              BoxOffice 实时票房（万） 
              MovieName 影片名 
              boxPer 票房占比 （%）
              movieDay 上映天数
              sumBoxOffice 累计票房（万） 
              time 数据获取时间
    """
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(ct.MOVIE_BOX%(ct.P_TYPE['http'], ct.DOMAINS['mbox'],
                              _random()))
            lines = urlopen(request, timeout = 10).read()
            if len(lines) < 15: #no data
                return None
        except Exception as e:
            print(e)
        else:
            js = json.loads(lines.decode('utf-8') if ct.PY3 else lines)
            df = pd.DataFrame(js['data2'])
            df = df.drop(['MovieImg','mId'], axis=1)
            df['time'] = du.get_now()
            return df


def day_boxoffice(date=None, retry_count=3,pause=0.001):
    """
    获取单日电影票房数据
    数据来源：EBOT艺恩票房智库
    Parameters
    ------
        date:日期，默认为上一日
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 
              AvgPrice 平均票价
              AvpPeoPle 场均人次
              BoxOffice 单日票房（万）
              BoxOffice_Up 环比变化 （%）
              MovieDay 上映天数
              MovieName 影片名 
              SumBoxOffice 累计票房（万） 
              WomIndex 口碑指数 
    """
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            if date is None:
                date = 0
            else:
                date = int(du.diff_day(du.today(), date)) + 1
                
            request = Request(ct.BOXOFFICE_DAY%(ct.P_TYPE['http'], ct.DOMAINS['mbox'],
                              date, _random()))
            lines = urlopen(request, timeout = 10).read()
            if len(lines) < 15: #no data
                return None
        except Exception as e:
            print(e)
        else:
            js = json.loads(lines.decode('utf-8') if ct.PY3 else lines)
            df = pd.DataFrame(js['data1'])
            df = df.drop(['MovieImg', 'BoxOffice1', 'MovieID', 'Director', 'IRank', 'IRank_pro'], axis=1)
            return df


def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

