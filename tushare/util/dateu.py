# -*- coding:utf-8 -*-

import datetime
import time
import pandas as pd


def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return[date[0:4], _quar(mon)]
    

def _quar(mon):
    if mon in [1, 2, 3]:
        return '1'
    elif mon in [4, 5, 6]:
        return '2'
    elif mon in [7, 8, 9]:
        return '3'
    elif mon in [10, 11, 12]:
        return '4'
    else:
        return None
 
 
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
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]

holiday = ['2015-01-01', '2015-01-02', '2015-02-18', '2015-02-19', '2015-02-20', '2015-02-23', '2015-02-24',
           '2015-04-06', '2015-05-01', '2015-06-22', '2015-09-03', '2015-09-04', '2015-10-01', '2015-10-02',
           '2015-10-05', '2015-10-06', '2015-10-07',
           '2016-01-01', '2016-02-08', '2016-02-09', '2016-02-10', '2016-02-11', '2016-02-12', '2016-04-04',
           '2016-05-02', '2016-06-09', '2016-06-10', '2016-09-15', '2016-09-16', '2016-10-03', '2016-10-04',
           '2016-10-05', '2016-10-06', '2016-10-07']


def is_holiday(date):
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
        
    

    
    