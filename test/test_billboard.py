from myshare.stock import billboard
from unittest import TestCase
import re


class TestBillboard(TestCase):
    def runTest(self):
        url = 'http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/' \
              'pagesize=200,page=1,sortRule=-1,sortType=,' \
              'startDate=2016-05-12,endDate=2016-05-12,gpfw=0,js=vardata_tab_1.html'
        result = billboard.request(url)
        print(result)
        regex = re.compile(b'\{.*\}')
        json = regex.search(result).group(0)
        print(json)
        assert result is not None
