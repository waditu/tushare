# -*- coding:utf-8 -*- 

DP_URL = '%sapp.finance.%s/data/stock/%s?day=&page=%s'
DP_163_URL = '%squotes.%s/data/caibao/%s?reportdate=%s&sort=declaredate&order=desc&page=%s'
DP_COLS = ['report_date', 'quarter', 'code', 'name', 'plan']
DP_163_COLS = ['code', 'name', 'year', 'plan', 'report_date']
DP_MSG = 'crawling the data %s ...'