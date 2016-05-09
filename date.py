# -*- coding:utf-8 -*-

import datetime
import time
import pandas
from myshare.stock import constants


def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return[date[0:4], _quar(mon)]
    

def quarter(mon):
    return mon // 4 + 1
 
 
def today():
    day = datetime.datetime.today().date()
    return str(day) 


def get_year():
    year = datetime.datetime.today().year
    return year


def get_month():
    month = datetime.datetime.today().month
    return month


def get_hour():
    return datetime.datetime.today().hour
    
    
def today_last_year():
    lasty = datetime.datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def day_last_week(days=-7):
    lasty = datetime.datetime.today().date() + datetime.timedelta(days)
    return str(lasty)


def get_now():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def diff_day(start=None, end=None):
    d1 = datetime.datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pandas.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def trade_calendar():
    '''
            交易日历
    isOpen=1是交易日，isOpen=0为休市
    '''
    df = pandas.read_csv(constants.ALL_CAL_FILE)
    return df


def is_holiday(date):
    '''
            判断是否为交易日，返回True or False
    '''
    df = trade_calendar()
    holiday = df[df.isOpen == 0]['calendarDate'].values
    if isinstance(date, str):
        today = datetime.datetime.strptime(date, '%Y-%m-%d')

    if today.isoweekday() in [6, 7] or date in holiday:
        return True
    else:
        return False


def last_tddate():
    today = datetime.datetime.today().date()
    today=int(today.strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)
        

    
    