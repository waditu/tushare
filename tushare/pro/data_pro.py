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
from tushare.util.formula import MA

PRICE_COLS = ['open', 'close', 'high', 'low']
FORMAT = lambda x: '%.2f' % x
FREQS = {'D': '1DAY',
         'W': '1WEEK',
         'Y': '1YEAR',
         }


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
        raise Exception('api init error.') 
        

def pro_bar(ts_code='', pro_api=None, start_date=None, end_date=None, freq='D', asset='E', 
           market='',
           adj = None,
           ma = [],
           retry_count = 3):
    """
    BAR数据
    Parameters:
    ------------
    ts_code:证券代码，支持股票,ETF/LOF,期货/期权,港股,数字货币
    start_date:开始日期  YYYYMMDD
    end_date:结束日期 YYYYMMDD
    freq:支持1/5/15/30/60分钟,周/月/季/年
    asset:证券类型 E:股票和交易所基金，I:沪深指数,C:数字货币,F:期货/期权/港股/中概美国/中证指数/国际指数
    market:市场代码，通过ts.get_markets()获取
    adj:复权类型,None不复权,qfq:前复权,hfq:后复权
    ma:均线,支持自定义均线频度，如：ma5/ma10/ma20/ma60/maN
    factors因子数据，目前支持以下两种：
        vr:量比,默认不返回，返回需指定：factor=['vr']
        tor:换手率，默认不返回，返回需指定：factor=['tor']
                    以上两种都需要：factor=['vr', 'tor']
    retry_count:网络重试次数
    
    Return
    ----------
    DataFrame
    code:代码
    open：开盘close/high/low/vol成交量/amount成交额/maN均价/vr量比/tor换手率
    
         期货(asset='X')
    code/open/close/high/low/avg_price：均价  position：持仓量  vol：成交总量
    """
    ts_code = ts_code.strip().upper()
    api = pro_api if pro_api is not None else pro_api()
    for _ in range(retry_count):
        try:
            freq = freq.strip().upper()
            asset = asset.strip().upper()
            if asset == 'E':
                if freq == 'D':
                    df = api.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
                    if adj is not None:
                        fcts = api.adj_factor(ts_code=ts_code, start_date=start_date, end_date=end_date)[['trade_date', 'adj_factor']]
                        data = df.set_index('trade_date', drop=False).merge(fcts.set_index('trade_date'), left_index=True, right_index=True, how='left')
                        data['adj_factor'] = data['adj_factor'].fillna(method='bfill')
                        for col in PRICE_COLS:
                            if adj == 'hfq':
                                data[col] = data[col] * data['adj_factor']
                            else:
                                data[col] = data[col] * data['adj_factor'] / float(fcts['adj_factor'][0])
                            data[col] = data[col].map(FORMAT)
                        data = data.drop('adj_factor', axis=1)
                    else:
                        data = df
                    if ma is not None and len(ma) > 0:
                        for a in ma:
                            if isinstance(a, int):
                                data['ma%s'%a] = MA(data['close'], a).map(FORMAT).shift(-(a-1))
                                data['ma%s'%a] = data['ma%s'%a].astype(float)
                    for col in PRICE_COLS:
                        data[col] = data[col].astype(float)
            if asset == 'I':
                if freq == 'D':
                    data = api.index_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            if asset == 'C':
                #//////////////////////// well soon
                pass
            return data
        except:
            return None
        else:
            return 
    raise IOError('ERROR.')


if __name__ == '__main__':
    pro = pro_api('fa381e2536d016fd126110367ac47cf9da5fa515a784a19cf38f5c41')
    print(pro_bar(ts_code='000001.SZ', pro_api=pro, start_date='19990101', end_date='', adj='qfq'))
#     print(pro_bar(ts_code='000905.SH', pro_api=pro, start_date='20181001', end_date='', asset='I'))
#     print(pro.trade_cal(exchange_id='', start_date='20131031', end_date='', fields='pretrade_date', is_open='0'))
    
    