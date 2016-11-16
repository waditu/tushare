# -*- coding:utf-8 -*- 
"""
基本面数据接口 
Created on 2015/01/18
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
import pandas as pd
from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re, demjson
from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

def get_stock_basics():
    """
        获取沪深上市公司基本情况
    Return
    --------
    DataFrame
               code,代码
               name,名称
               industry,细分行业
               area,地区
               pe,市盈率
               outstanding,流通股本
               totals,总股本(万)
               totalAssets,总资产(万)
               liquidAssets,流动资产
               fixedAssets,固定资产
               reserved,公积金
               reservedPerShare,每股公积金
               eps,每股收益
               bvps,每股净资
               pb,市净率
               timeToMarket,上市日期
    """
    request = Request(ct.ALL_STOCK_BASICS_FILE)
    text = urlopen(request, timeout=10).read()
    text = text.decode('GBK')
    text = text.replace('--', '')
    df = pd.read_csv(StringIO(text), dtype={'code':'object'})
    df = df.set_index('code')
    return df


def get_report_data(year, quarter):
    """
        获取业绩报表数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        eps,每股收益
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
    """
    if ct._check_input(year,quarter) is True:
        ct._write_head()
        df =  _get_report_data(year, quarter, 1, pd.DataFrame())
        if df is not None:
#             df = df.drop_duplicates('code')
            df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        return df


def _get_report_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.REPORT_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], ct.PAGES['fd'],
                         year, quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df = df.drop(11, axis=1)
        df.columns = ct.REPORT_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_report_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)


def get_profit_data(year, quarter):
    """
        获取盈利能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        roe,净资产收益率(%)
        net_profit_ratio,净利率(%)
        gross_profit_rate,毛利率(%)
        net_profits,净利润(万元)
        eps,每股收益
        business_income,营业收入(百万元)
        bips,每股主营业务收入(元)
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        data =  _get_profit_data(year, quarter, 1, pd.DataFrame())
        if data is not None:
#             data = data.drop_duplicates('code')
            data['code'] = data['code'].map(lambda x:str(x).zfill(6))
        return data


def _get_profit_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.PROFIT_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                              ct.PAGES['fd'], year,
                                              quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df.columns=ct.PROFIT_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_profit_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except:
        pass


def get_operation_data(year, quarter):
    """
        获取营运能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        arturnover,应收账款周转率(次)
        arturndays,应收账款周转天数(天)
        inventory_turnover,存货周转率(次)
        inventory_days,存货周转天数(天)
        currentasset_turnover,流动资产周转率(次)
        currentasset_days,流动资产周转天数(天)
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        data =  _get_operation_data(year, quarter, 1, pd.DataFrame())
        if data is not None:
#             data = data.drop_duplicates('code')
            data['code'] = data['code'].map(lambda x:str(x).zfill(6))
        return data


def _get_operation_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.OPERATION_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                                 ct.PAGES['fd'], year,
                                                 quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df.columns=ct.OPERATION_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_operation_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)


def get_growth_data(year, quarter):
    """
        获取成长能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        mbrg,主营业务收入增长率(%)
        nprg,净利润增长率(%)
        nav,净资产增长率
        targ,总资产增长率
        epsg,每股收益增长率
        seg,股东权益增长率
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        data =  _get_growth_data(year, quarter, 1, pd.DataFrame())
        if data is not None:
#             data = data.drop_duplicates('code')
            data['code'] = data['code'].map(lambda x:str(x).zfill(6))
        return data


def _get_growth_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.GROWTH_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                              ct.PAGES['fd'], year,
                                              quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df.columns=ct.GROWTH_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_growth_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)


def get_debtpaying_data(year, quarter):
    """
        获取偿债能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        currentratio,流动比率
        quickratio,速动比率
        cashratio,现金比率
        icratio,利息支付倍数
        sheqratio,股东权益比率
        adratio,股东权益增长率
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        df =  _get_debtpaying_data(year, quarter, 1, pd.DataFrame())
        if df is not None:
#             df = df.drop_duplicates('code')
            df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        return df


def _get_debtpaying_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.DEBTPAYING_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                                  ct.PAGES['fd'], year,
                                                  quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df.columns = ct.DEBTPAYING_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_debtpaying_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)
 
 
def get_cashflow_data(year, quarter):
    """
        获取现金流量数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
       
    Return
    --------
    DataFrame
        code,代码
        name,名称
        cf_sales,经营现金净流量对销售收入比率
        rateofreturn,资产的经营现金流量回报率
        cf_nm,经营现金净流量与净利润的比率
        cf_liabilities,经营现金净流量对负债比率
        cashflowratio,现金流量比率
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        df =  _get_cashflow_data(year, quarter, 1, pd.DataFrame())
        if df is not None:
#             df = df.drop_duplicates('code')
            df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        return df


def _get_cashflow_data(year, quarter, pageNo, dataArr):
    ct._write_console()
    try:
        request = Request(ct.CASHFLOW_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                                ct.PAGES['fd'], year,
                                                quarter, pageNo, ct.PAGE_NUM[1]))
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df.columns = ct.CASHFLOW_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_cashflow_data(year, quarter, pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)
       
       
def _data_path():
    import os
    import inspect
    caller_file = inspect.stack()[1][1]  
    pardir = os.path.abspath(os.path.join(os.path.dirname(caller_file), os.path.pardir))
    return os.path.abspath(os.path.join(pardir, os.path.pardir))

def get_stock_intro(code):
    '''
    股票简介
    来源: http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/000001.phtml
    Parameters
    --------
        code:股票代码
    Return
    --------
        name:公司名称
        listed_market:上市市场
        listed_date:上市日期
        offering_price:发行价格
        found_date:成立日期
        registered_capital:注册资本
        company_tel:公司电话
        company_url:公司网址
        rename_history:证券简称更名历史
        office_address:办公地址
        company_profile:公司简介
        business_scope:经营范围
    '''
    symbol = code
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/%s.phtml' % (symbol)
    res = lxml.html.parse(url).xpath('//table[@id="comInfo1"]/tr')
    if res and len(res) == 21:
        name = res[0].xpath('td/text()')[1]

        listed_market = res[2].xpath('td/text()')[1]
        listed_date = res[2].xpath('td/a/text()')[0]

        offering_price = res[3].xpath('td/text()')[1]

        found_date = res[4].xpath('td/a/text()')[0]
        registered_capital = res[4].xpath('td/text()')[2]

        company_tel = res[6].xpath('td/text()')[3]

        company_url = res[12].xpath('td/a/text()')[0]
        rename_history = res[16].xpath('td/text()')[1]
        office_address = res[18].xpath('td/text()')[1]
        company_profile = res[19].xpath('td/text()')[1]
        business_scope = res[20].xpath('td/text()')[1]

        return pd.DataFrame([[name, listed_market, listed_date, offering_price, found_date, registered_capital, company_tel, company_url, rename_history, office_address, company_profile, business_scope]],
            columns=['name', 'listed_market', 'listed_date', 'offering_price', 'found_date', 'registered_capital', 'company_tel', 'company_url', 'rename_history', 'office_address', 'company_profile', 'business_scope'])


def get_stock_preliminary_earnings_estimate(code, num='all'):
    '''
    个股业绩快报(营业收入,净利润,现金流量)
    来源: http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/scbhz/index.phtml?symbol=000001
    内容: 股票代码 股票名称 财报日期 批露日期 每股收益(元) 营业收入 净利润 每股净资产(元) 净资产收益率(%) 每股现金流量(元) 毛利率(%) 分配方案 明细 PDF报告
    Parameters
    --------
        code:股票代码
        num:数量
    Return
    --------
        code:股票代码
        name:股票名称
        date:财报日期
        operation_revenue:营业收入(万元)
        retained_profits:净利润(万元)
        cash_flow:每股现金流量(元)
    '''
    symbol = code
    url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/scbhz/index.phtml?symbol=%s' % (symbol)
    res = lxml.html.parse(url).xpath('//div[@id="box"]/table/tbody/tr')
    data = []
    for td in res:
        dl = td.xpath('td')
        if len(dl) == 16:
            code = dl[0].xpath('a/text()')[0]
            name = dl[1].xpath('a/text()')[0]
            date = dl[2].text
            operation_revenue = dl[5].text
            retained_profits = dl[7].text
            cash_flow = dl[11].text
            data.append([code, name, date, operation_revenue, retained_profits, cash_flow])
            if len(data) >= num:
                break
    df = pd.DataFrame(data, columns=['code', 'name', 'date', 'operation_revenue', 'retained_profits', 'cash_flow'])
    return df

def get_stock_list(page='all', limit=100, ispd=False):
    '''
    A股列表
    来源: http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?&node=hs_a&symbol=&_s_r_a=page&sort=code&asc=1&num=100&page=1
    网页：http://vip.stock.finance.sina.com.cn/mkt/#stock_hs_up
    内容:
    Parameters
    --------
        page:取多少页
        limit:每页条数
    Return
    --------

    '''
    dataList = []
    i = 1
    while 1:
        url = 'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?&node=hs_a&symbol=&_s_r_a=page&sort=code&asc=1&num=%s&page=%s' % (limit, i)
        data = urlopen(Request(url), timeout=30).read().decode('gbk')
        jdata = demjson.decode(data)
        dataList += jdata
        i += 1
        if i > page or len(jdata) < limit:
            break
    return pd.DataFrame(dataList) if ispd else dataList