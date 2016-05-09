import time
from datetime import datetime


def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return[date[0:4], _quar(mon)]

def today():
    day = datetime.today().date()
    print day.type()

