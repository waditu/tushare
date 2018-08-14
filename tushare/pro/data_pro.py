# -*- coding:utf-8 -*- 
"""
pro init 
Created on 2018/07/01
@author: Jimmy Liu
@group : tushare.pro
@contact: jimmysoa@sina.cn
"""

from tushare.pro import client
from tushare.util import upass

def pro_api(token=''):
    """
    初始化pro API,第一次可以通过ts.set_token('your token')来记录自己的token凭证，临时token可以通过本参数传入
    """
    if token == '' or token is None:
        token = upass.get_token()
    if token is not None and token != '':
        pro = client.DataApi(token)
        return pro
    else:
        exit(0) 
        

if __name__ == '__main__':
    pro = pro_api()
    print(pro.trade_cal(exchange_id='', start_date='20131031', end_date='', fields='pretrade_date', is_open='0'))
    
    