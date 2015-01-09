# -*- coding:utf-8 -*- 
'''
Created on 2013/07/31
@author: Jimmy Liu
'''

DAY_PRICE_COLUMNS = ['date','open','high','close','low','amount','price_change','p_change','ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover']
TICK_COLUMNS = ['time','price','change','volume','cash','type']
TICK_PRICE_URL = 'http://market.finance.sina.com.cn/downxls.php?date=%s&symbol=%s'
DAY_PRICE_URL = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last'
SINA_DAY_PRICE_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page&page=%s'
DAY_TRADING_COLUMNS = ['code','symbol','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio']
DAY_PRICE_PAGES = 38