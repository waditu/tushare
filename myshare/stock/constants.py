# -*- coding:utf-8 -*-
"""
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
import sys

VERSION = '0.3.6'
K_LABELS = ['D', 'W', 'M']
MINUTE_K_TYPE = ['5', '15', '30', '60']
K_TYPE = {'day': 'akdaily', 'week': 'akweekly', 'month': 'akmonthly'}
INDEX_LABELS = ['sh', 'sz', 'hs300', 'sz50', 'cyb', 'zxb', 'zx300', 'zh500']
INDEX_LIST = {'sh': 'sh000001', 'sz': 'sz399001', 'hs300': 'sz399300',
              'sz50': 'sh000016', 'zxb': 'sz399005', 'cyb': 'sz399006', 'zx300': 'sz399008', 'zh500':'sh000905'}
PROTOCOLS = {'http': 'http://', 'ftp': 'ftp://'}
PAGE_NUM = [38, 60, 80, 100]
DOMAINS = {'sina': 'sina.com.cn', 'sinahq': 'sinajs.cn',
           'ifeng': 'ifeng.com', 'sf': 'finance.sina.com.cn',
           'vsf': 'vip.stock.finance.sina.com.cn',
           'idx': 'www.csindex.com.cn', '163': 'money.163.com',
           'east': 'eastmoney.com', 'sseq': 'query.sse.com.cn',
           'sse': 'www.sse.com.cn', 'szse': 'www.szse.cn',
           'oss': '218.244.146.57', 'idxip':'115.29.204.48',
           'shibor': 'www.shibor.org', 'mbox':'www.cbooo.cn'}
PAGES = {'fd': 'index.phtml', 'dl': 'downxls.php', 'jv': 'json_v2.php',
         'cpt': 'newFLJK.php', 'ids': 'newSinaHy.php', 'lnews':'rollnews_ch_out_interface.php',
         'ntinfo':'vCB_BulletinGather.php', 'hs300b':'000300cons.xls',
         'hs300w':'000300closeweight.xls','sz50b':'000016cons.xls',
         'dp':'all_fpya.php', '163dp':'fpyg.html',
         'emxsg':'JS.aspx', '163fh':'jjcgph.php',
         'newstock':'vRPD_NewStockIssue.php', 'zz500b':'000905cons.xls',
         'zz500wt':'000905closeweight.xls',
         't_ticks':'vMS_tradedetail.php', 'dw': 'downLoad.html',
         'qmd':'queryMargin.do', 'szsefc':'ShowReport.szse',
         'ssecq':'commonQuery.do', 'sinadd':'cn_bill_download.php', 'ids_sw':'SwHy.php'}
TICK_COLUMNS = ['time', 'price', 'change', 'volume', 'amount', 'type']
TODAY_TICK_COLUMNS = ['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type']
DAY_TRADING_COLUMNS = ['code', 'symbol', 'name', 'changepercent',
                       'trade', 'open', 'high', 'low', 'settlement', 'volume', 'turnoverratio',
                       'amount', 'per', 'pb', 'mktcap', 'nmc']
REPORT_COLS = ['code', 'name', 'eps', 'eps_yoy', 'bvps', 'roe',
               'epcf', 'net_profits', 'profits_yoy', 'distrib', 'report_date']
FORECAST_COLS = ['code', 'name', 'type', 'report_date', 'pre_eps', 'range']
PROFIT_COLS = ['code', 'name', 'roe', 'net_profit_ratio',
               'gross_profit_rate', 'net_profits', 'eps', 'business_income', 'bips']
OPERATION_COLS = ['code', 'name', 'arturnover', 'arturndays', 'inventory_turnover',
                  'inventory_days', 'currentasset_turnover', 'currentasset_days']
GROWTH_COLS = ['code', 'name', 'mbrg', 'nprg', 'nav', 'targ', 'epsg', 'seg']
DEBTPAYING_COLS = ['code', 'name', 'currentratio',
                   'quickratio', 'cashratio', 'icratio', 'sheqratio', 'adratio']
CASHFLOW_COLS = ['code', 'name', 'cf_sales', 'rateofreturn',
                 'cf_nm', 'cf_liabilities', 'cashflowratio']
DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                     'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']
INX_DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                         'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20']
LIVE_DATA_COLS = ['name', 'open', 'pre_close', 'price', 'high', 'low', 'bid', 'ask', 'volume', 'amount',
                  'b1_v', 'b1_p', 'b2_v', 'b2_p', 'b3_v', 'b3_p', 'b4_v', 'b4_p', 'b5_v', 'b5_p',
                  'a1_v', 'a1_p', 'a2_v', 'a2_p', 'a3_v', 'a3_p', 'a4_v', 'a4_p', 'a5_v', 'a5_p', 'date', 'time', 's']
FOR_CLASSIFY_B_COLS = ['code','name']
FOR_CLASSIFY_W_COLS = ['date','code', 'weight']
FOR_CLASSIFY_W5_COLS = ['date','code', 'name', 'weight']
THE_FIELDS = [
    'code', 'symbol', 'name', 'changepercent', 'trade', 'open', 'high', 'low', 'settlement', 'volume', 'turnoverratio']
TICK_PRICE_URL = '%smarket.%s/%s?date=%s&symbol=%s'
TODAY_TICKS_PAGE_URL = '%s%s/quotes_service/api/%s/CN_Transactions.getAllPageTime?date=%s&symbol=%s'
TODAY_TICKS_URL = '%s%s/quotes_service/view/%s?symbol=%s&date=%s&page=%s'
# DAY_PRICE_URL = '%sapi.finance.%s/%s/?code=%s&type=last'
DAY_PRICE_URL = 'http://api.finance.ifeng.com/%s/?code=%s&type=last'
DAY_PRICE_MIN_URL = 'http://api.finance.ifeng.com/akmin?scode=%s&type=%s'
LIVE_DATA_URL = '%shq.%s/rn=%s&list=%s'
SINA_DAY_PRICE_URL = '%s%s/quotes_service/api/%s/Market_Center.getHQNodeData?num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page&page=%s'
REPORT_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/mainindex/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
FORECAST_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/performance/%s?s_i=&s_a=&s_c=&s_type=&reportdate=%s&quarter=%s&p=%s&num=%s'
PROFIT_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/profit/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
OPERATION_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/operation/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
GROWTH_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/grow/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
DEBTPAYING_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/debtpaying/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
CASHFLOW_URL = '%s%s/q/go.php/vFinanceAnalyze/kind/cashflow/%s?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
SHIBOR_TYPE ={'Shibor': 'Shibor数据', 'Quote': '报价数据', 'Tendency': 'Shibor均值数据',
              'LPR': 'LPR数据', 'LPR_Tendency': 'LPR均值数据'}
SHIBOR_DATA_URL = '%s%s/shibor/web/html/%s?nameNew=Historical_%s_Data_%s.xls&downLoadPath=data&nameOld=%s%s.xls&shiborSrc=http://www.shibor.org/shibor/'
ALL_STOCK_BASICS_FILE = '%s%s/static/all.csv'%(PROTOCOLS['http'], DOMAINS['oss'])
ALL_CAL_FILE = '%s%s/static/calAll.csv'%(PROTOCOLS['http'], DOMAINS['oss'])
SINA_CONCEPTS_INDEX_URL = '%smoney.%s/q/view/%s?param=class'
SINA_INDUSTRY_INDEX_URL = '%s%s/q/view/%s'
SINA_DATA_DETAIL_URL = '%s%s/quotes_service/api/%s/Market_Center.getHQNodeData?page=1&num=1000&sort=symbol&asc=1&node=%s&symbol=&_s_r_a=page'
INDEX_C_COMM = 'sseportal/ps/zhs/hqjt/csi'
HS300_CLASSIFY_URL_FTP = '%s%s/webdata/%s'
HS300_CLASSIFY_URL_HTTP = '%s%s/%s/%s'
HIST_FQ_URL = '%s%s/corp/go.php/vMS_FuQuanMarketHistory/stockid/%s.phtml?year=%s&jidu=%s'
HIST_INDEX_URL = '%s%s/corp/go.php/vMS_MarketHistory/stockid/%s/type/S.phtml?year=%s&jidu=%s'
HIST_FQ_FACTOR_URL = '%s%s/api/json.php/BasicStockSrv.getStockFuQuanData?symbol=%s&type=hfq'
INDEX_HQ_URL = '''%shq.%s/rn=xppzh&list=sh000001,sh000002,sh000003,sh000008,sh000009,sh000010,sh000011,sh000012,sh000016,sh000017,sh000300,sz399001,sz399002,sz399003,sz399004,sz399005,sz399006,sz399100,sz399101,sz399106,sz399107,sz399108,sz399333,sz399606'''
SSEQ_CQ_REF_URL = '%s%s/assortment/stock/list/name'
ALL_STK_URL = '%s%s/all.csv'
SINA_DD = '%s%s/quotes_service/view/%s?symbol=%s&num=60&page=1&sort=ticktime&asc=0&volume=%s&amount=0&type=0&day=%s'
BOX = 'boxOffice'
MOVIE_BOX = '%s%s/%s/GetHourBoxOffice?d=%s'
BOXOFFICE_DAY = '%s%s/%s/GetDayBoxOffice?num=%s&d=%s'
BOXOFFICE_MONTH = '%s%s/%s/getMonthBox?sdate=%s'
BOXOFFICE_CBD = '%s%s/%s/getCBD?pIndex=%s&dt=%s'
SHIBOR_COLS = ['date', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
QUOTE_COLS = [
    'date', 'bank', 'ON_B', 'ON_A', '1W_B', '1W_A', '2W_B', '2W_A', '1M_B', '1M_A',
    '3M_B', '3M_A', '6M_B', '6M_A', '9M_B', '9M_A', '1Y_B', '1Y_A']
SHIBOR_MA_COLS = ['date', 'ON_5', 'ON_10', 'ON_20', '1W_5', '1W_10', '1W_20','2W_5', '2W_10', '2W_20',
                  '1M_5', '1M_10', '1M_20', '3M_5', '3M_10', '3M_20', '6M_5', '6M_10', '6M_20',
                  '9M_5', '9M_10', '9M_20','1Y_5', '1Y_10', '1Y_20']
LPR_COLS = ['date', '1Y']
LPR_MA_COLS = ['date', '1Y_5', '1Y_10', '1Y_20']
INDEX_HEADER = 'code,name,open,preclose,close,high,low,0,0,volume,amount,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,d,c,3\n'
INDEX_COLS = ['code', 'name', 'change', 'open', 'preclose', 'close', 'high', 'low', 'volume', 'amount']
HIST_FQ_COLS = ['date', 'open', 'high', 'close', 'low', 'volume', 'amount', 'factor']
SINA_DD_COLS = ['code', 'name', 'time', 'price', 'volume', 'preprice', 'type']
HIST_FQ_FACTOR_COLS = ['code', 'value']
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
DATA_ROWS_TIPS = '%s rows data found.Please wait for a moment.'
DATA_INPUT_ERROR_MSG = 'date input error.'
NETWORK_URL_ERROR_MSG = '获取失败，请检查网络和URL'
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
TOP_PARAS_MSG = 'top有误，请输入整数或all.'
LHB_MSG = '周期输入有误，请输入数字5、10、30或60'
TOKEN_F_P = 'tk.csv'
TOKEN_ERR_MSG = '请设置通联数据接口的token凭证码'
BOX_INPUT_ERR_MSG = '请输入YYYY-MM格式的年月数据'

# IS_PY3 = (sys.version_info[0] >= 3)

# -*- coding:utf-8 -*-

DP_URL = '%sapp.finance.%s/data/stock/%s?day=&page=%s'
DP_163_URL = '%squotes.%s/data/caibao/%s?reportdate=%s&sort=declaredate&order=desc&page=%s'
FUND_HOLDS_URL = '%squotes.%s/hs/marketdata/service/%s?host=/hs/marketdata/service/%s&page=%s&query=start:%s;end:%s&order=desc&count=60&type=query&req=%s'
XSG_URL = '%sdatainterface.%s/EM_DataCenter/%s?type=FD&sty=BST&st=3&sr=true&fd=%s&stat=%s'

# 龙虎榜
# LHB_URL = '%sdata.%s/stock/lhb/%s.html'
LHB_URL = '%sdata.%s/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=%s,endDate=%s,gpfw=0,js=vardata_tab_1.html'
LHB_SINA_URL = '%s%s/q/go.php/vLHBData/kind/%s/%s?last=%s&p=%s'
LHB_SINA_URL_GG = 'http://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/ggtj/index.phtml?last=%s&p=%s'
LHB_EAST_COLS = ['SCode', 'SName', 'Chgradio', 'ZeMoney', 'Bmoney', 'Smoney', 'Ctypedes', 'Turnover']
LHB_COLS = ['code', 'name', 'pchange', 'amount', 'buy', 'sell', 'reason', 'turnover']
LHB_KINDS = ['ggtj', 'yytj', 'jgzz', 'jgmx']
LHB_GGTJ_COLS = ['code', 'name', 'count', 'buy_amount', 'sell_amount', 'net', 'buy_seats', 'sell_seats']
LHB_YYTJ_COLS = ['broker', 'count', 'bamount', 'bcount', 'samount', 'scount', 'top3']
LHB_JGZZ_COLS = ['code', 'name', 'bamount', 'bcount', 'samount', 'scount', 'net']
LHB_JGMX_COLS = ['code', 'name', 'date', 'bamount', 'samount', 'type']

NEW_STOCKS_URL = '%s%s/corp/view/%s?page=%s&cngem=0&orderBy=NetDate&orderType=desc'
MAR_SH_HZ_URL = '%s%s/marketdata/tradedata/%s?jsonCallBack=jsonpCallback%s&isPagination=true&tabType=&pageHelp.pageSize=100&beginDate=%s&endDate=%s%s&_=%s'
MAR_SH_HZ_REF_URL = '%s%s/market/dealingdata/overview/margin/'
MAR_SH_MX_URL = '%s%s/marketdata/tradedata/%s?jsonCallBack=jsonpCallback%s&isPagination=true&tabType=mxtype&detailsDate=%s&pageHelp.pageSize=100&stockCode=%s&beginDate=%s&endDate=%s%s&_=%s'
MAR_SZ_HZ_URL = '%s%s/szseWeb/%s?SHOWTYPE=EXCEL&ACTIONID=8&CATALOGID=1837_xxpl&txtDate=%s&tab2PAGENUM=1&ENCODE=1&TABKEY=tab1'
MAR_SZ_MX_URL = '%s%s/szseWeb/%s?SHOWTYPE=EXCEL&ACTIONID=8&CATALOGID=1837_xxpl&txtDate=%s&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2'
MAR_SH_HZ_TAIL_URL = '&pageHelp.pageNo=%s&pageHelp.beginPage=%s&pageHelp.endPage=%s'
TERMINATED_URL = '%s%s/%s?jsonCallBack=jsonpCallback%s&isPagination=true&sqlId=COMMON_SSE_ZQPZ_GPLB_MCJS_ZZSSGGJBXX_L&pageHelp.pageSize=50&_=%s'
SUSPENDED_URL = '%s%s/%s?jsonCallBack=jsonpCallback%s&isPagination=true&sqlId=COMMON_SSE_ZQPZ_GPLB_MCJS_ZTSSGS_L&pageHelp.pageSize=50&_=%s'
TERMINATED_T_COLS = ['COMPANY_CODE', 'COMPANY_ABBR', 'LISTING_DATE', 'CHANGE_DATE']

TERMINATED_COLS = ['code', 'name', 'oDate', 'tDate']
DP_COLS = ['report_date', 'quarter', 'code', 'name', 'plan']
DP_163_COLS = ['code', 'name', 'year', 'plan', 'report_date']
XSG_COLS = ['code', 'name', 'date', 'count', 'ratio']
QUARTS_DIC = {'1':('%s-12-31', '%s-03-31'), '2':('%s-03-31', '%s-06-30'),
              '3':('%s-06-30', '%s-09-30'), '4':('%s-9-30', '%s-12-31')}
FUND_HOLDS_COLS = ['count', 'clast', 'date', 'ratio', 'amount', 'nums','nlast', 'name', 'code']
NEW_STOCKS_COLS = ['code', 'name', 'ipo_date', 'issue_date', 'amount', 'markets', 'price', 'pe',
                   'limit', 'funds', 'ballot']
MAR_SH_COOKIESTR = '_gscu_1808689395=27850607moztu036'
MAR_SH_HZ_COLS = ['opDate', 'rzye', 'rzmre', 'rqyl', 'rqylje', 'rqmcl', 'rzrqjyzl']
MAR_SH_MX_COLS = ['opDate', 'stockCode', 'securityAbbr', 'rzye', 'rzmre', 'rzche', 'rqyl', 'rqmcl', 'rqchl']
MAR_SZ_HZ_COLS = ['rzmre', 'rzye', 'rqmcl', 'rqyl', 'rqye', 'rzrqye']
MAR_SZ_MX_COLS = ['stockCode', 'securityAbbr', 'rzmre', 'rzye', 'rqmcl', 'rqyl', 'rqye', 'rzrqye']
MAR_SZ_HZ_MSG = 'please do not input more than a year,you can obtaining the data year by year.'
MAR_SZ_HZ_MSG2 = 'start and end date all need input.'


def two_decimal(x): return '%.2f' % x
FORMAT4 = lambda x: '%.4f' % x


def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()


def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()


def _write_tips(tip):
    sys.stdout.write(DATA_ROWS_TIPS%tip)
    sys.stdout.flush()


def console_write(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


def _check_input(year, quarter):
    if isinstance(year, str) or year < 1989 :
        raise TypeError(DATE_CHK_MSG)
    elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
        raise TypeError(DATE_CHK_Q_MSG)
    else:
        return True


# def _check_lhb_input(last):
#     if last not in [5, 10, 30, 60]:
#         raise TypeError(LHB_MSG)
#     else:
#         return True