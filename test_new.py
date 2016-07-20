import tushare as ts
import pandas as pd

from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re
from pandas.compat import StringIO

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


df = ts.get_debtpaying_data(year=2016,quarter=1,orderby='errors')
print (df)
df.to_excel('/Users/elliot/Downloads/debtpaying_data2016Q1.xlsx')

"""
year=2016
quarter=1
orderby='default'
pageNo=1

urla=(ct.PROFIT_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                           ct.PAGES['fd'], year,
                                           quarter, pageNo, ct.PAGE_NUM[1], orderby))

print (urla)
"""