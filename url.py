# -*- coding:utf-8 -*-

import pandas as pd
from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re
from pandas.compat import StringIO

year=2016
quarter=1
pageNo=1


print ("stock_basics:",(ct.ALL_STOCK_BASICS_FILE))

print ("get_report_data:",(ct.REPORT_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'], ct.PAGES['fd'],
                                           year, quarter, pageNo, ct.PAGE_NUM[1])))


print ("get_profit_data:",(ct.PROFIT_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                           ct.PAGES['fd'], year,
                                           quarter, pageNo, ct.PAGE_NUM[1])))


print ("get_operation_data:",(ct.OPERATION_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                              ct.PAGES['fd'], year,
                                              quarter, pageNo, ct.PAGE_NUM[1])))

print ("get_growth_data:",(ct.GROWTH_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                           ct.PAGES['fd'], year,
                                           quarter, pageNo, ct.PAGE_NUM[1])))

print ("debtpaying_data:",(ct.DEBTPAYING_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                               ct.PAGES['fd'], year,
                                               quarter, pageNo, ct.PAGE_NUM[1])))




#get_report_data
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=2016&quarter=1&p=1&num=60&order=code%7C1
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=2016&quarter=1&p=1&num=60
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=2016&quarter=1&p=4&num=60&order=code%7C1

#get_profit_data
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=2016&quarter=1&p=1&num=60


#get_operation_data
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml?s_i=&s_a=&s_c=&reportdate=2016&quarter=1&p=1&num=60

#get_growth_data

#debtpaying_data



