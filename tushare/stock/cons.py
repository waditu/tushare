# -*- coding:utf-8 -*- 
"""
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

def data_path():
    import os
    import inspect
    caller_file = inspect.stack()[1][1]  
    pardir = os.path.abspath(os.path.join(os.path.dirname(caller_file), os.path.pardir))
    return os.path.abspath(os.path.join(pardir, os.path.pardir))

VERSION = '0.1.5'
K_LABELS = ['D','W','M']
K_MIN_LABELS = ['5','15','30','60']
K_TYPE = {'D':'akdaily','W':'akweekly','M':'akmonthly'}
INDEX_LABELS = ['sh','sz','hs300','sz50','cyb','zxb']
INDEX_LIST = {'sh':'sh000001','sz':'sz399001','hs300':'sz399300','sz50':'sh000016','cyb':'sz399005','zxb':'sz399006'}
P_TYPE = {'http':'http://','ftp':'ftp://'}
DAY_PRICE_PAGES = 38
DOMAINS = {'sina':'sina.com.cn','sinahq':'sinajs.cn','ifeng':'ifeng.com'}
TICK_COLUMNS = ['time','price','change','volume','amount','type']
DAY_TRADING_COLUMNS = ['code','symbol','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio']
REPORT_COLS = ['code','name','eps','eps_yoy','bvps','roe','epcf','net_profits','profits_yoy','distrib','report_date']
FORECAST_COLS = ['code','name','type','report_date','pre_eps','range']
PROFIT_COLS = ['code','name','roe','net_profit_ratio','gross_profit_rate','net_profits','eps','business_income','bips']
OPERATION_COLS = ['code', 'name','arturnover','arturndays','inventory_turnover','inventory_days','currentasset_turnover','currentasset_days']
GROWTH_COLS = ['code','name','mbrg','nprg','nav','targ','epsg','seg']
DEBTPAYING_COLS = ['code','name','currentratio','quickratio','cashratio','icratio','sheqratio','adratio']
CASHFLOW_COLS = ['code','name','cf_sales','rateofreturn','cf_nm','cf_liabilities','cashflowratio']
DAY_PRICE_COLUMNS = ['date','open','high','close','low','volume','price_change','p_change',
                     'ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover']
INX_DAY_PRICE_COLUMNS = ['date','open','high','close','low','volume','price_change','p_change',
                     'ma5','ma10','ma20','v_ma5','v_ma10','v_ma20']
LIVE_DATA_COLS = ['name','open','pre_close','price','high','low','bid','ask','volume','amount',
               'b1_v','b1_p','b2_v','b2_p','b3_v','b3_p','b4_v','b4_p','b5_v','b5_p',
               'a1_v','a1_p','a2_v','a2_p','a3_v','a3_p','a4_v','a4_p','a5_v','a5_p','date','time','s']
TICK_PRICE_URL = '%smarket.finance.%s/downxls.php?date=%s&symbol=%s'
DAY_PRICE_URL = '%sapi.finance.%s/%s/?code=%s&type=last'
LIVE_DATA_URL = '%shq.%s/rn=%s&list=%s'
DAY_PRICE_MIN_URL = '%sapi.finance.%s/akmin?scode=%s&type=%s'
SINA_DAY_PRICE_URL = '%svip.stock.finance.%s/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page&page=%s'
REPORT_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
FORECAST_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=%s&quarter=%s&p=%s&num=60'
PROFIT_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
OPERATION_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/operation/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
GROWTH_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/grow/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
DEBTPAYING_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
CASHFLOW_URL = '%svip.stock.finance.%s/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=60'
ALL_STOCK_BASICS_FILE = '%s/tushare/data/all.csv'%data_path()