# -*- coding:utf-8 -*- 

DP_URL = '%sapp.finance.%s/data/stock/%s?day=&page=%s'
DP_163_URL = '%squotes.%s/data/caibao/%s?reportdate=%s&sort=declaredate&order=desc&page=%s'
DP_COLS = ['report_date', 'quarter', 'code', 'name', 'plan']
DP_163_COLS = ['code', 'name', 'year', 'plan', 'report_date']
XSG_URL = '%sdatainterface.%s/EM_DataCenter/%s?type=FD&sty=BST&st=3&sr=true&fd=%s&stat=%s'
XSG_COLS = ['code', 'name', 'date', 'count', 'ratio']
QUARTS_DIC = {'1':('%s-12-31', '%s-03-31'), '2':('%s-03-31', '%s-06-30'), 
              '3':('%s-06-30', '%s-09-30'), '4':('%s-9-30', '%s-12-31')}
FUND_HOLDS_URL = '%squotes.%s/hs/marketdata/service/%s?host=/hs/marketdata/service/%s&page=%s&query=start:%s;end:%s&order=desc&count=60&type=query&req=%s'
FUND_HOLDS_COLS = ['count', 'clast', 'date', 'ratio', 'amount', 'nums','nlast', 'name', 'code']
NEW_STOCKS_URL = '%s%s/corp/view/%s?page=%s&cngem=0&orderBy=NetDate&orderType=desc'
NEW_STOCKS_COLS = ['code', 'name', 'ipo_date', 'issue_date', 'amount', 'markets', 'price', 'pe',
                   'limit', 'funds', 'ballot']