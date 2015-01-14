# -*- coding:utf-8 -*- 
"""
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

DAY_PRICE_COLUMNS = ['date','open','high','close','low','amount','price_change','p_change','ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover']
TICK_COLUMNS = ['time','price','change','volume','amount','type']
TICK_PRICE_URL = 'http://market.finance.sina.com.cn/downxls.php?date=%s&symbol=%s'
DAY_PRICE_URL = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last'
LIVE_DATA_URL = 'http://hq.sinajs.cn/list=%s'
SINA_DAY_PRICE_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page&page=%s'
DAY_TRADING_COLUMNS = ['code','symbol','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio']
DAY_PRICE_PAGES = 38
LIVE_DATA_COLS = ['name','open','pre_close','price','high','low','bid','ask','volume','amount',
               'b1_v','b1_p','b2_v','b2_p','b3_v','b3_p','b4_v','b4_p','b5_v','b5_p',
               'a1_v','a1_p','a2_v','a2_p','a3_v','a3_p','a4_v','a4_p','a5_v','a5_p','date','time','s']
