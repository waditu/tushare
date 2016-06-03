# -*- coding:utf-8 -*- 
"""
交易数据接口 
Created on 2014/07/31
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import constants
import numpy
from enum import Enum
from io import BytesIO
import json
import lxml.html
from lxml import etree
import pandas
from myshare.util import net
import time
import re


# MinutesKLineType = Enum('KLineType', 'day, week, month, five_minutes, fifteen_minutes, thirty_minutes, sixty_minutes')


def get_history_data(code=None, start=None, end=None, k_line='day', retry_count=3, pause=0.001):
    """
        获取个股历史交易记录
    Parameters
    ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取到API所提供的最早日期数据
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取到最近一个交易日数据
      k_line:string
                  数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    return
    -------
      DataFrame
          属性:日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率
    """
    symbol = _code_to_symbol(code)
    k_line = k_line.lower()
    _is_minutes_k_line = is_minutes_k_line(k_line)

    if _is_minutes_k_line:
        url = constants.DAY_PRICE_URL % (constants.K_TYPE[k_line], symbol)
    else:
        url = constants.DAY_PRICE_MIN_URL % (symbol, k_line)
    
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            html = net.request(url, 'utf-8')
            if len(html) < 15: #no data
                return None
        except Exception as e:
            print(e)
        else:
            _json = json.loads(html)

            cols = constants.DAY_PRICE_COLUMNS

            if len(_json['record'][0]) == 14 | (code in constants.INDEX_LABELS & (not _is_minutes_k_line)):
                # remove column turnover
                cols = cols[:-1]

            data_frame = pandas.DataFrame(_json['record'], columns=cols)

            if not _is_minutes_k_line:
                data_frame = data_frame.applymap(lambda x: x.replace(u',', u''))
                data_frame[data_frame == ''] = 0

            for col in cols[1:]:
                data_frame[col] = data_frame[col].astype(float)
            if start is not None:
                data_frame = data_frame[data_frame.date >= start]
            if end is not None:
                data_frame = data_frame[data_frame.date <= end]
            if (code in constants.INDEX_LABELS) & (k_line in constants.K_MIN_LABELS):
                data_frame = data_frame.drop('turnover', axis=1)
            data_frame = data_frame.set_index('date')
            data_frame = data_frame.sort_index(ascending=False)
            return data_frame
    raise IOError(constants.NETWORK_URL_ERROR_MSG)


def is_minutes_k_line(k_line):
    k_line = k_line.lower()
    if k_line in constants.MINUTE_K_TYPE():
        return True
    if k_line in constants.K_TYPE.keys():
        return False
    raise TypeError('k_line type error.')


def _parsing_dayprice_json(pageNum=1):
    """
           处理当日行情分页数据，格式为json
     Parameters
     ------
        pageNum:页码
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
    """
    constants._write_console()
    request = Request(constants.SINA_DAY_PRICE_URL%(constants.P_TYPE['http'], constants.DOMAINS['vsf'],
                                 constants.PAGES['jv'], pageNum))
    text = urlopen(request, timeout=10).read()
    if text == 'null':
        return None
    reg = re.compile(r'\,(.*?)\:') 
    text = reg.sub(r',"\1":', text.decode('gbk') if constants.PY3 else text) 
    text = text.replace('"{symbol', '{"symbol')
    text = text.replace('{symbol', '{"symbol"')
    if constants.PY3:
        jstr = json.dumps(text)
    else:
        jstr = json.dumps(text, encoding='GBK')
    js = json.loads(jstr)
    df = pd.DataFrame(pd.read_json(js, dtype={'code':object}),
                      columns=constants.DAY_TRADING_COLUMNS)
    df = df.drop('symbol', axis=1)
#     df = df.ix[df.volume > 0]
    return df


def get_tick_data(code=None, date=None, retry_count=3, pause=0.001):
    """
        获取分笔数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        date:string
                  日期 format：YYYY-MM-DD
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    if code is None or len(code)!=6 or date is None:
        return None
    symbol = _code_to_symbol(code)
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            re = Request(constants.TICK_PRICE_URL % (constants.P_TYPE['http'], constants.DOMAINS['sf'], constants.PAGES['dl'],
                                date, symbol))
            lines = urlopen(re, timeout=10).read()
            lines = lines.decode('GBK') 
            if len(lines) < 20:
                return None
            df = pd.read_table(StringIO(lines), names=constants.TICK_COLUMNS,
                               skiprows=[0])      
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(constants.NETWORK_URL_ERROR_MSG)


def get_sina_dd(code=None, date=None, vol=400, retry_count=3, pause=0.001):
    """
        获取sina大单数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        date:string
                  日期 format：YYYY-MM-DD
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:股票代码    股票名称    交易时间    价格    成交量    前一笔价格    类型（买、卖、中性盘）
    """
    if code is None or len(code)!=6 or date is None:
        return None
    symbol = _code_to_symbol(code)
    vol = vol*100
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            re = Request(constants.SINA_DD % (constants.P_TYPE['http'], constants.DOMAINS['vsf'], constants.PAGES['sinadd'],
                                symbol, vol, date))
            lines = urlopen(re, timeout=10).read()
            lines = lines.decode('GBK') 
            if len(lines) < 100:
                return None
            df = pd.read_csv(StringIO(lines), names=constants.SINA_DD_COLS,
                               skiprows=[0])    
            if df is not None:
                df['code'] = df['code'].map(lambda x: x[2:])
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(constants.NETWORK_URL_ERROR_MSG)


def get_today_ticks(code=None, retry_count=3, pause=0.001):
    """
        获取当日分笔明细数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    if code is None or len(code)!=6 :
        return None
    symbol = _code_to_symbol(code)
    date = du.today()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(constants.TODAY_TICKS_PAGE_URL % (constants.P_TYPE['http'], constants.DOMAINS['vsf'],
                                                       constants.PAGES['jv'], date,
                                                       symbol))
            data_str = urlopen(request, timeout=10).read()
            data_str = data_str.decode('GBK')
            data_str = data_str[1:-1]
            data_str = eval(data_str, type('Dummy', (dict,), 
                                           dict(__getitem__ = lambda s, n:n))())
            data_str = json.dumps(data_str)
            data_str = json.loads(data_str)
            pages = len(data_str['detailPages'])
            data = pd.DataFrame()
            constants._write_head()
            for pNo in range(1, pages+1):
                data = data.append(_today_ticks(symbol, date, pNo,
                                                retry_count, pause), ignore_index=True)
        except Exception as er:
            print(str(er))
        else:
            return data
    raise IOError(constants.NETWORK_URL_ERROR_MSG)


def _today_ticks(symbol, tdate, pageNo, retry_count, pause):
    constants._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            html = lxml.html.parse(constants.TODAY_TICKS_URL % (constants.P_TYPE['http'],
                                                         constants.DOMAINS['vsf'], constants.PAGES['t_ticks'],
                                                         symbol, tdate, pageNo
                                ))  
            res = html.xpath('//table[@id=\"datatbl\"]/tbody/tr')
            if constants.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            sarr = sarr.replace('--', '0')
            df = pd.read_html(StringIO(sarr), parse_dates=False)[0]
            df.columns = constants.TODAY_TICK_COLUMNS
            df['pchange'] = df['pchange'].map(lambda x : x.replace('%', ''))
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(constants.NETWORK_URL_ERROR_MSG)
        
    
def get_today_all():
    """
        一次性获取最近一个日交易日所有股票的交易数据
    return
    -------
      DataFrame
           属性：代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值
    """
    constants._write_head()
    df = _parsing_dayprice_json(1)
    if df is not None:
        for i in range(2, constants.PAGE_NUM[0]):
            newdf = _parsing_dayprice_json(i)
            df = df.append(newdf, ignore_index=True)
    return df


def get_realtime_quotes(symbols=None):
    """
        获取实时交易数据 getting real time quotes data
       用于跟踪交易情况（本次执行的结果-上一次执行的数据）
    Parameters
    ------
        symbols : string, array-like object (list, tuple, Series).
        
    return
    -------
        DataFrame 实时交易数据
              属性:0：name，股票名字
            1：open，今日开盘价
            2：pre_close，昨日收盘价
            3：price，当前价格
            4：high，今日最高价
            5：low，今日最低价
            6：bid，竞买价，即“买一”报价
            7：ask，竞卖价，即“卖一”报价
            8：volumn，成交量 maybe you need do volumn/100
            9：amount，成交金额（元 CNY）
            10：b1_v，委买一（笔数 bid volume）
            11：b1_p，委买一（价格 bid price）
            12：b2_v，“买二”
            13：b2_p，“买二”
            14：b3_v，“买三”
            15：b3_p，“买三”
            16：b4_v，“买四”
            17：b4_p，“买四”
            18：b5_v，“买五”
            19：b5_p，“买五”
            20：a1_v，委卖一（笔数 ask volume）
            21：a1_p，委卖一（价格 ask price）
            ...
            30：date，日期；
            31：time，时间；
    """
    symbols_list = ''
    if isinstance(symbols, list) or isinstance(symbols, set) or isinstance(symbols, tuple) or isinstance(symbols, pd.Series):
        for code in symbols:
            symbols_list += _code_to_symbol(code) + ','
    else:
        symbols_list = _code_to_symbol(symbols)
        
    symbols_list = symbols_list[:-1] if len(symbols_list) > 8 else symbols_list 
    request = Request(constants.LIVE_DATA_URL%(constants.P_TYPE['http'], constants.DOMAINS['sinahq'],
                                                _random(), symbols_list))
    text = urlopen(request,timeout=10).read()
    text = text.decode('GBK')
    reg = re.compile(r'\="(.*?)\";')
    data = reg.findall(text)
    regSym = re.compile(r'(?:sh|sz)(.*?)\=')
    syms = regSym.findall(text)
    data_list = []
    syms_list = []
    for index, row in enumerate(data):
        if len(row)>1:
            data_list.append([astr for astr in row.split(',')])
            syms_list.append(syms[index])
    if len(syms_list) == 0:
        return None
    df = pd.DataFrame(data_list, columns=constants.LIVE_DATA_COLS)
    df = df.drop('s', axis=1)
    df['code'] = syms_list
    ls = [cls for cls in df.columns if '_v' in cls]
    for txt in ls:
        df[txt] = df[txt].map(lambda x : x[:-2])
    return df


def get_h_data(code, start=None, end=None, autype='qfq',
               index=False, retry_count=3, pause=0.001, drop_factor=True):
    '''
    获取历史复权数据
    Parameters
    ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取当前日期
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取去年今日
      autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数 
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
      drop_factor : bool, 默认 True
                是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活
    return
    -------
      DataFrame
          date 交易日期 (index)
          open 开盘价
          high  最高价
          close 收盘价
          low 最低价
          volume 成交量
          amount 成交金额
    '''
    
    start = du.today_last_year() if start is None else start
    end = du.today() if end is None else end
    qs = du.get_quarts(start, end)
    qt = qs[0]
    constants._write_head()
    data = _parse_fq_data(_get_index_url(index, code, qt), index,
                          retry_count, pause)
    if len(qs)>1:
        for d in range(1, len(qs)):
            qt = qs[d]
            constants._write_console()
            df = _parse_fq_data(_get_index_url(index, code, qt), index,
                                retry_count, pause)
            if df is None:  # 可能df为空，退出循环
                break
            else:
                data = data.append(df, ignore_index=True)
    if len(data) == 0 or len(data[(data.date>=start)&(data.date<=end)]) == 0:
        return None
    data = data.drop_duplicates('date')
    if index:
        data = data[(data.date>=start) & (data.date<=end)]
        data = data.set_index('date')
        data = data.sort_index(ascending=False)
        return data
    if autype == 'hfq':
        if drop_factor:
            data = data.drop('factor', axis=1)
        data = data[(data.date>=start) & (data.date<=end)]
        for label in ['open', 'high', 'close', 'low']:
            data[label] = data[label].map(constants.FORMAT)
            data[label] = data[label].astype(float)
        data = data.set_index('date')
        data = data.sort_index(ascending = False)
        return data
    else:
        if autype == 'qfq':
            if drop_factor:
                data = data.drop('factor', axis=1)
            df = _parase_fq_factor(code, start, end)
            df = df.drop_duplicates('date')
            df = df.sort('date', ascending=False)
            firstDate = data.head(1)['date']
            frow = df[df.date == firstDate[0]]
            rt = get_realtime_quotes(code)
            if rt is None:
                return None
            if ((float(rt['high']) == 0) & (float(rt['low']) == 0)):
                preClose = float(rt['pre_close'])
            else:
                if du.is_holiday(du.today()):
                    preClose = float(rt['price'])
                else:
                    if (du.get_hour() > 9) & (du.get_hour() < 18):
                        preClose = float(rt['pre_close'])
                    else:
                        preClose = float(rt['price'])
            
            rate = float(frow['factor']) / preClose
            data = data[(data.date >= start) & (data.date <= end)]
            for label in ['open', 'high', 'low', 'close']:
                data[label] = data[label] / rate
                data[label] = data[label].map(constants.FORMAT)
                data[label] = data[label].astype(float)
            data = data.set_index('date')
            data = data.sort_index(ascending = False)
            return data
        else:
            for label in ['open', 'high', 'close', 'low']:
                data[label] = data[label] / data['factor']
            if drop_factor:
                data = data.drop('factor', axis=1)
            data = data[(data.date>=start) & (data.date<=end)]
            for label in ['open', 'high', 'close', 'low']:
                data[label] = data[label].map(constants.FORMAT)
            data = data.set_index('date')
            data = data.sort_index(ascending = False)
            data = data.astype(float)
            return data


def _parase_fq_factor(code, start, end):
    symbol = _code_to_symbol(code)
    request = Request(constants.HIST_FQ_FACTOR_URL%(constants.P_TYPE['http'],
                                             constants.DOMAINS['vsf'], symbol))
    text = urlopen(request, timeout=10).read()
    text = text[1:len(text)-1]
    text = text.decode('utf-8') if constants.PY3 else text
    text = text.replace('{_', '{"')
    text = text.replace('total', '"total"')
    text = text.replace('data', '"data"')
    text = text.replace(':"', '":"')
    text = text.replace('",_', '","')
    text = text.replace('_', '-')
    text = json.loads(text)
    df = pd.DataFrame({'date':list(text['data'].keys()), 'factor':list(text['data'].values())})
    df['date'] = df['date'].map(_fun_except) # for null case
    if df['date'].dtypes == np.object:
        df['date'] = df['date'].astype(np.datetime64)
    df = df.drop_duplicates('date')
    df['factor'] = df['factor'].astype(float)
    return df


def _fun_except(x):
    if len(x) > 10:
        return x[-10:]
    else:
        return x


def _parse_fq_data(url, index, retry_count, pause):
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(url)
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath('//table[@id=\"FundHoldSharesTable\"]')
            if constants.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            df = pd.read_html(sarr, skiprows = [0, 1])[0]
            if len(df) == 0:
                return pd.DataFrame()
            if index:
                df.columns = constants.HIST_FQ_COLS[0:7]
            else:
                df.columns = constants.HIST_FQ_COLS
            if df['date'].dtypes == np.object:
                df['date'] = df['date'].astype(np.datetime64)
            df = df.drop_duplicates('date')
        except ValueError as e:
            # 时间较早，已经读不到数据
            return None
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(constants.NETWORK_URL_ERROR_MSG)


def get_index():
    """
    获取大盘指数行情
    return
    -------
      DataFrame
          code:指数代码
          name:指数名称
          change:涨跌幅
          open:开盘价
          preclose:昨日收盘价
          close:收盘价
          high:最高价
          low:最低价
          volume:成交量(手)
          amount:成交金额（亿元）
    """
    request = Request(constants.INDEX_HQ_URL%(constants.P_TYPE['http'],
                                             constants.DOMAINS['sinahq']))
    text = urlopen(request, timeout=10).read()
    text = text.decode('GBK')
    text = text.replace('var hq_str_sh', '').replace('var hq_str_sz', '')
    text = text.replace('";', '').replace('"', '').replace('=', ',')
    text = '%s%s'%(constants.INDEX_HEADER, text)
    df = pd.read_csv(StringIO(text), sep=',', thousands=',')
    df['change'] = (df['close'] / df['preclose'] - 1 ) * 100
    df['amount'] = df['amount'] / 100000000
    df['change'] = df['change'].map(constants.FORMAT)
    df['amount'] = df['amount'].map(constants.FORMAT4)
    df = df[constants.INDEX_COLS]
    df['code'] = df['code'].map(lambda x:str(x).zfill(6))
    df['change'] = df['change'].astype(float)
    df['amount'] = df['amount'].astype(float)
    return df
 

def _get_index_url(index, code, qt):
    if index:
        url = constants.HIST_INDEX_URL%(constants.P_TYPE['http'], constants.DOMAINS['vsf'],
                              code, qt[0], qt[1])
    else:
        url = constants.HIST_FQ_URL%(constants.P_TYPE['http'], constants.DOMAINS['vsf'],
                              code, qt[0], qt[1])
    return url


def get_hists(symbols, start=None, end=None,
                  k_line='D', retry_count=3,
                  pause=0.001):
    """
    批量获取历史行情数据，具体参数和返回数据类型请参考get_hist_data接口
    """
    df = pd.DataFrame()
    if isinstance(symbols, list) or isinstance(symbols, set) or isinstance(symbols, tuple) or isinstance(symbols, pd.Series):
        for symbol in symbols:
            data = get_hist_data(symbol, start=start, end=end,
                                 k_line=k_line, retry_count=retry_count,
                                 pause=pause)
            data['code'] = symbol
            df = df.append(data, ignore_index=True)
        return df
    else:
        return None
    
    
def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))


def _code_to_symbol(code):
    """
        生成symbol代码标志
    """
    if code in constants.INDEX_LABELS:
        return constants.INDEX_LIST[code]

    if len(code) == 8 & code[:2].lower() in ['sh', 'sz']:
        return code

    if len(code) == 6:
        return 'sh%s' % code if code[:1] in ['5', '6', '9'] else 'sz%s' % code

    return ''
