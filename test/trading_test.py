# -*- coding:utf-8 -*- 

import tushare.stock.trading as td

if __name__ == '__main__':
    print td.get_tick_data('600848', '2015-01-09')