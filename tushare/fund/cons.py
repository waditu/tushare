# -*- coding:utf-8 -*-
"""
Created on 2016/04/03
@author: Leo
@group : lazytech
@contact: lazytech@sina.cn
"""

VERSION = '0.0.1'
K_LABELS = ['D', 'W', 'M']
K_MIN_LABELS = ['5', '15', '30', '60']
K_TYPE = {'D': 'akdaily', 'W': 'akweekly', 'M': 'akmonthly'}
INDEX_LABELS = ['sh', 'sz', 'hs300', 'sz50', 'cyb', 'zxb']
INDEX_LIST = {'sh': 'sh000001', 'sz': 'sz399001', 'hs300': 'sz399300',
              'sz50': 'sh000016', 'zxb': 'sz399005', 'cyb': 'sz399006'}
P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
PAGE_NUM = [38, 60, 80, 100]
FORMAT = lambda x: '%.2f' % x
DOMAINS = {'sina': 'sina.com.cn', 'sinahq': 'sinajs.cn',
           'ifeng': 'ifeng.com', 'sf': 'finance.sina.com.cn',
           'ssf': 'stock.finance.sina.com.cn',
           'vsf': 'vip.stock.finance.sina.com.cn',
           'idx': 'www.csindex.com.cn', '163': 'money.163.com',
           'em': 'eastmoney.com', 'sseq': 'query.sse.com.cn',
           'sse': 'www.sse.com.cn', 'szse': 'www.szse.cn',
           'oss': '218.244.146.57',
           'shibor': 'www.shibor.org'}
PAGES = {'fd': 'index.phtml', 'dl': 'downxls.php', 'jv': 'json_v2.php',
         'cpt': 'newFLJK.php', 'ids': 'newSinaHy.php', 'lnews':'rollnews_ch_out_interface.php',
         'ntinfo':'vCB_BulletinGather.php', 'hs300b':'000300cons.xls',
         'hs300w':'000300closeweight.xls','sz50b':'000016cons.xls',
         'dp':'all_fpya.php', '163dp':'fpyg.html',
         'emxsg':'JS.aspx', '163fh':'jjcgph.php',
         'newstock':'vRPD_NewStockIssue.php', 'zz500b':'000905cons.xls',
         't_ticks':'vMS_tradedetail.php', 'dw': 'downLoad.html',
         'qmd':'queryMargin.do', 'szsefc':'FrontController.szse',
         'ssecq':'commonQuery.do'}

NAV_OPEN_API = { 'all':'getNetValueOpen','equity':'getNetValueOpen','mix':'getNetValueOpen','bond':'getNetValueOpen','monetary':'getNetValueMoney','qdii':'getNetValueOpen',
                    'close':'getNetValueClose','cx':'getNetValueCX'}

NAV_OPEN_KEY = {'all':'6XxbX6h4CED0ATvW','equity':'Gb3sH5uawH5WCUZ9','mix':'6XxbX6h4CED0ATvW',
                'bond':'Gb3sH5uawH5WCUZ9','monetary':'uGo5qniFnmT5eQjp','qdii':'pTYExKwRmqrSaP0P'}
NAV_OPEN_TYPE2 = { 'all':'0','equity':'2','mix':'1','bond':'3','monetary':'0','qdii':'6'}
#NAV_OPEN_TYPE3 = {}

#=====================================================================================================================================================================
#基金数据列名

NAV_OPEN_COLUMNS = ['symbol','sname','per_nav','total_nav','yesterday_nav','nav_rate','nav_a','nav_date','fund_manager','jjlx','jjzfe']

NAV_HIS_JJJZ = ['fbrq','jjjz','ljjz']
NAV_HIS_NHSY = ['fbrq','nhsyl','dwsy']

FUND_INFO_COLS = ['symbol','jjqc','jjjc','clrq','ssrq','xcr','ssdd',\
                  'Type1Name','Type2Name','Type3Name','jjgm','jjfe',\
                  'jjltfe','jjferq','quarter','glr','tgr']

#=====================================================================================================================================================================
#数据源URL
SINA_NAV_COUNT_URL = '%s%s/fund_center/data/jsonp.php/IO.XSRV2.CallbackList[\'%s\']/NetValue_Service.%s?ccode=&type2=%s&type3='
SINA_NAV_DATA_URL = '%s%s/fund_center/data/jsonp.php/IO.XSRV2.CallbackList[\'%s\']/NetValue_Service.%s?page=1&num=%s&ccode=&type2=%s&type3=' 

SINA_NAV_HISTROY_COUNT_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=%s&datefrom=%s&dateto=%s'
SINA_NAV_HISTROY_DATA_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=%s&datefrom=%s&dateto=%s&num=%s'


SINA_NAV_HISTROY_COUNT_CUR_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNavcur?symbol=%s&datefrom=%s&dateto=%s'
SINA_NAV_HISTROY_DATA_CUR_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNavcur?symbol=%s&datefrom=%s&dateto=%s&num=%s'

SINA_DATA_DETAIL_URL = '%s%s/quotes_service/api/%s/Market_Center.getHQNodeData?page=1&num=400&sort=symbol&asc=1&node=%s&symbol=&_s_r_a=page'

SINA_FUND_INFO_URL = '%s%s/fundInfo/api/openapi.php/FundPageInfoService.tabjjgk?symbol=%s&format=json'

#=====================================================================================================================================================================

SHIBOR_COLS = ['date', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
QUOTE_COLS = ['date', 'bank', 'ON_B', 'ON_A', '1W_B', '1W_A', '2W_B', '2W_A', '1M_B', '1M_A',
                    '3M_B', '3M_A', '6M_B', '6M_A', '9M_B', '9M_A', '1Y_B', '1Y_A']
SHIBOR_MA_COLS = ['date', 'ON_5', 'ON_10', 'ON_20', '1W_5', '1W_10', '1W_20','2W_5', '2W_10', '2W_20',
                  '1M_5', '1M_10', '1M_20', '3M_5', '3M_10', '3M_20', '6M_5', '6M_10', '6M_20',
                  '9M_5', '9M_10', '9M_20','1Y_5', '1Y_10', '1Y_20']
LPR_COLS = ['date', '1Y']
LPR_MA_COLS = ['date', '1Y_5', '1Y_10', '1Y_20']
INDEX_HEADER = 'code,name,open,preclose,close,high,low,0,0,volume,amount,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,d,c,3\n'
INDEX_COLS = ['code', 'name', 'change', 'open', 'preclose', 'close', 'high', 'low', 'volume', 'amount']

HIST_FQ_FACTOR_COLS = ['code','value']
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
DATA_ROWS_TIPS = '%s rows data found.Please wait for a moment.'
DATA_INPUT_ERROR_MSG = 'date input error.'
NETWORK_URL_ERROR_MSG = '获取失败，请检查网络和URL'
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
TOP_PARAS_MSG = 'top有误，请输入整数或all.'
LHB_MSG = '周期输入有误，请输入数字5、10、30或60'

OFT_MSG = u'开放型基金类型输入有误，请输入all、equity、mix、bond、monetary、qdii'

DICT_NAV_EQUITY = {
    'fbrq':'date',
    'jjjz':'value',
    'ljjz':'total',
    'change':'change'
} 

DICT_NAV_MONETARY = {
    'fbrq':'date',
    'nhsyl':'value',
    'dwsy':'total' 
} 

import sys
PY3 = (sys.version_info[0] >= 3)
def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()

def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()
    
def _write_tips(tip):
    sys.stdout.write(DATA_ROWS_TIPS%tip)
    sys.stdout.flush()

def _write_msg(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()   
    
def _check_input(year, quarter):
    if isinstance(year, str) or year < 1989 :
        raise TypeError(DATE_CHK_MSG)
    elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
        raise TypeError(DATE_CHK_Q_MSG)
    else:
        return True
    
def _check_nav_oft_input(found_type):
    if found_type not in NAV_OPEN_KEY.keys():
        raise TypeError(OFT_MSG)
    else:
        return True

def _check_input(year, quarter):
    if isinstance(year, str) or year < 1989 :
        raise TypeError(DATE_CHK_MSG)
    elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
        raise TypeError(DATE_CHK_Q_MSG)
    else:
        return True        