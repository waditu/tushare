# -*- coding:utf-8 -*- 

DP_URL = '%sapp.finance.%s/data/stock/%s?day=&page=%s'
DP_163_URL = '%squotes.%s/data/caibao/%s?reportdate=%s&sort=declaredate&order=desc&page=%s'
FUND_HOLDS_URL = '%squotes.%s/hs/marketdata/service/%s?host=/hs/marketdata/service/%s&page=%s&query=start:%s;end:%s&order=desc&count=60&type=query&req=%s'
XSG_URL = '%sdatainterface.%s/EM_DataCenter/%s?type=FD&sty=BST&st=3&sr=true&fd=%s&stat=%s'
# LHB_URL = '%sdata.%s/stock/lhb/%s.html'
LHB_URL = '%sdata.%s/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=%s,endDate=%s,gpfw=0,js=vardata_tab_1.html'
LHB_SINA_URL = '%s%s/q/go.php/vLHBData/kind/%s/%s?last=%s&p=%s'
LHB_TMP_COLS = ['SCode', 'SName', 'Chgradio', 'ZeMoney', 'Bmoney', 'Smoney', 'Ctypedes', 'Turnover']
LHB_COLS = ['code', 'name', 'pchange', 'amount', 'buy', 'sell', 'reason', 'Turnover']
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
LHB_KINDS = ['ggtj', 'yytj', 'jgzz', 'jgmx']
LHB_GGTJ_COLS = ['code', 'name', 'count', 'bamount', 'samount', 'net', 'bcount', 'scount']
LHB_YYTJ_COLS = ['broker', 'count', 'bamount', 'bcount', 'samount', 'scount', 'top3']
LHB_JGZZ_COLS = ['code', 'name', 'bamount', 'bcount', 'samount', 'scount', 'net']
LHB_JGMX_COLS = ['code', 'name', 'date', 'bamount', 'samount', 'type']
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
