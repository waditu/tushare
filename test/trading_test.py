# -*- coding:utf-8 -*- 

# import tushare.stock.trading as td
import tushare as ts

if __name__ == '__main__':
#     print td.get_tick_data('600848', '2015-01-09')
#     print td.get_realtime_quotes('600848')
#     print td.get_realtime_quotes(['600848','000980','000981'])
#     df = td.get_today_all()
#     print td.get_realtime_quotes(df['code'].tail(10))
    print ts.get_hist_data('600848',start='2015-02-25')