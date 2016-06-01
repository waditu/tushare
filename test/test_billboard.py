from myshare.stock import billboard
from myshare.stock import constants
from myshare.util import date_helper
from unittest import TestCase
import pandas
import re


class TestBillboard(TestCase):
    # def test_request(self):
        # url = 'http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/' \
        #       'pagesize=200,page=1,sortRule=-1,sortType=,' \
        #       'startDate=2016-05-12,endDate=2016-05-12,gpfw=0,js=vardata_tab_1.html'
        # result = billboard.request(url)
        # print(result)
        # regex = re.compile('\{.*\}')
        # json = regex.search(result).group(0)
        # print(json)
        # assert result is not None

    # def test_decode_json(self):
    #     date = date_helper.last_trade_date()
    #     url = constants.LHB_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['east'], date, date)
    #     content = billboard.lhb_info(url)
    #     print(type(content))
    #     assert content is not None

    def test_data_frame(self):
        # date = date_helper.last_trade_date()
        # date = '2016-05-27'
        # url = constants.LHB_URL % (constants.PROTOCOLS['http'], constants.DOMAINS['east'], date, date)
        # lhb_data = billboard.lhb_info(url)
        # data_frame = pandas.DataFrame(lhb_data['data'], columns=constants.LHB_TMP_COLS)
        # data_frame.columns = constants.LHB_COLS
        # data_frame['buy'] = data_frame['buy'].astype(float)
        # print(data_frame['buy'])
        # billboard.top_list(date)
        # assert data_frame['buy'] is not None
        # url = constants.LHB_SINA_URL_GG % (billboard.LhbPeriod.five, 1)
        # html = billboard.request(url)
        # print(html)
        billboard.stock_tops_page()

