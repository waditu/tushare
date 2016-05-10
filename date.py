# -*- coding:utf-8 -*-

import time
import pandas
from datetime import datetime
from datetime import timedelta
from myshare.stock import constants


def year_quarter(date):
    mon = date[5:7]
    mon = int(mon)
    return[date[0:4], _quar(mon)]
    

def quarter(mon):
    return mon // 4 + 1
 
 
def today():
    day = datetime.today().date()
    return str(day) 


def get_year():
    year = datetime.today().year
    return year


def get_month():
    month = datetime.today().month
    return month


def get_hour():
    return datetime.today().hour
    
    
def same_day_last_year():
    return str(datetime.today().date() + timedelta(-365))


def same_day_last_week():
    return str(datetime.today().date() + timedelta(-7))


def get_now():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def diff_day(start=None, end=None):
    d1 = datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pandas.period_range(
        'Q'.join(year_quarter(start)),
        'Q'.join(year_quarter(end)),
        freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def trade_calendar():
    # 交易日历
    # isOpen=1是交易日，isOpen=0为休市
    df = pandas.read_csv(constants.ALL_CAL_FILE)
    return df


def is_holiday(date):
    # 判断是否为交易日，返回True or False
    df = trade_calendar()
    holiday = df[df.isOpen == 0]['calendarDate'].values
    if isinstance(date, str):
        _today = datetime.strptime(date, '%Y-%m-%d')

    if _today.isoweekday() > 5 or date in holiday:
        return True
    else:
        return False


def last_tddate():
    _today = int(datetime.today().date().strftime("%w"))
    if _today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)