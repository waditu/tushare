# -*- coding:utf-8 -*- 
"""
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

DAY_PRICE_COLUMNS = ['date','open','high','close','low','volume','price_change','p_change','ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover']
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
S_ALL_URL = 'http://qd.baidupcs.com/file/fbe04e7078534b760661785ad70c27a9?bkt=p2-qd-104&fid=722398329-250528-322845645363958&time=1421658506&sign=FDTAXERLBH-DCb740ccc5511e5e8fedcff06b081203-5VmkuJGofGeR3oJK2j7THCjYUjw%3D&to=qb&fm=Qin,B,U,nc&newver=1&newfm=1&flow_ver=3&sl=81723466&expires=8h&rt=sh&r=503386760&mlogid=4000075416&vuk=722398329&vbdid=1465029029&fin=all.csv&fn=all.csv'
REPORT_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
FORECAST_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=%s&quarter=%s&p=%s&num=60'
REPORT_COLS = ['code','name','eps','eps_yoy','bvps','roe','epcf','net_profits','profits_yoy','distrib','report_date']
def data_path():
    import os
    import inspect
    caller_file = inspect.stack()[1][1]  # caller's filename
    pardir = os.path.abspath(os.path.join(os.path.dirname(caller_file), os.path.pardir))
    return os.path.abspath(os.path.join(pardir, os.path.pardir))

ALL_STOCK_BASICS_FILE = '%s/data/all.csv'%data_path()