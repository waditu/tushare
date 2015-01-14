# -*- coding:utf-8 -*- 

import tushare.stock.trading as td

if __name__ == '__main__':
#     print td.get_tick_data('600848', '2015-01-09')
    print td.get_realtime_quotes('600848')
    print td.get_realtime_quotes(['600848','000980','000981'])
#     df = td.get_today_all()
#     print td.get_realtime_quotes(df['code'].tail(10))