# -*- coding:utf-8 -*- 

import datetime
import pandas as pd


def year_qua(date):
    mon = date[4:6]
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


def diff_day(start=None, end=None):
    d1 = datetime.datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


holiday = ['2015-01-01', '2015-01-02', '2015-02-18', '2015-02-19', '2015-02-20', '2015-02-23', '2015-02-24', '2015-04-06',
                            '2015-05-01', '2015-06-22', '2015-09-03',  '2015-09-04', '2015-10-01', '2015-10-02', '2015-10-05', '2015-10-06', '2015-10-07']
    

def is_holiday(date):
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    today=int(date.strftime("%w"))
    if today > 0 and today < 6 and date not in holiday:
        return False
    else:
        return True
    
    
def last_tddate():
    today = datetime.datetime.today().date()
    today=int(today.strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)
        
    

    
    
