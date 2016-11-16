# -*- coding:utf-8 -*-

"""
新闻事件数据接口 
Created on 2015/02/07
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

from tushare.stock import cons as ct
from tushare.stock import news_vars as nv
import pandas as pd
from datetime import datetime
import lxml.html
from lxml import etree
import re
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request



def get_latest_news(top=None, show_content=False):
    """
        获取即时财经新闻
    
    Parameters
    --------
        top:数值，显示最新消息的条数，默认为80条
        show_content:是否显示新闻内容，默认False
    
    Return
    --------
        DataFrame
            classify :新闻类别
            title :新闻标题
            time :发布时间
            url :新闻链接
            content:新闻内容（在show_content为True的情况下出现）
    """
    top = ct.PAGE_NUM[2] if top is None else top
    try:
        request = Request(nv.LATEST_URL % (ct.P_TYPE['http'], ct.DOMAINS['sina'],
                                                   ct.PAGES['lnews'], top,
                                                   _random()))
        data_str = urlopen(request, timeout=10).read()
        data_str = data_str.decode('GBK')
        data_str = data_str.split('=')[1][:-1]
        data_str = eval(data_str, type('Dummy', (dict,), 
                                       dict(__getitem__ = lambda s, n:n))())
        data_str = json.dumps(data_str)
        data_str = json.loads(data_str)
        data_str = data_str['list']
        data = []
        for r in data_str:
            rt = datetime.fromtimestamp(r['time'])
            rtstr = datetime.strftime(rt, "%m-%d %H:%M")
            arow = [r['channel']['title'], r['title'], rtstr, r['url']]
            if show_content:
                arow.append(latest_content(r['url']))
            data.append(arow)
        df = pd.DataFrame(data, columns=nv.LATEST_COLS_C if show_content else nv.LATEST_COLS)
        return df
    except Exception as er:
        print(str(er))


def latest_content(url):
    '''
        获取即时财经新闻内容
    Parameter
    --------
        url:新闻链接
    
    Return
    --------
        string:返回新闻的文字内容
    '''
    try:
        html = lxml.html.parse(url)
        res = html.xpath('//div[@id=\"artibody\"]/p')
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr).replace('&#12288;', '')#.replace('\n\n', '\n').
        html_content = lxml.html.fromstring(sarr)
        content = html_content.text_content()
        return content
    except Exception as er:
        print(str(er))  


def get_notices(code=None, date=None):
    '''
    个股信息地雷
    Parameters
    --------
        code:股票代码
        date:信息公布日期
    
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        type:信息类型
        date:公告日期
        url:信息内容URL
    '''
    if code is None:
        return None
    symbol = 'sh' + code if code[:1] == '6' else 'sz' + code
    url = nv.NOTICE_INFO_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                              ct.PAGES['ntinfo'], symbol)
    url = url if date is None else '%s&gg_date=%s'%(url, date)
    html = lxml.html.parse(url)
    res = html.xpath('//table[@class=\"body_table\"]/tbody/tr')
    data = []
    for td in res:
        title = td.xpath('th/a/text()')[0]
        type = td.xpath('td[1]/text()')[0]
        date = td.xpath('td[2]/text()')[0]
        url = '%s%s%s'%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], td.xpath('th/a/@href')[0])
        data.append([title, type, date, url])
    df = pd.DataFrame(data, columns=nv.NOTICE_INFO_CLS)
    return df


def notice_content(url):
    '''
        获取信息地雷内容
    Parameter
    --------
        url:内容链接
    
    Return
    --------
        string:信息内容
    '''
    try:
        html = lxml.html.parse(url)
        res = html.xpath('//div[@id=\"content\"]/pre/text()')[0]
        return res.strip()
    except Exception as er:
        print(str(er))  


def guba_sina(show_content=False):
    """
       获取sina财经股吧首页的重点消息
    Parameter
    --------
        show_content:是否显示内容，默认False
    
    Return
    --------
    DataFrame
        title, 消息标题
        content, 消息内容（show_content=True的情况下）
        ptime, 发布时间
        rcounts,阅读次数
    """
    
    from pandas.io.common import urlopen
    try:
        with urlopen(nv.GUBA_SINA_URL%(ct.P_TYPE['http'],
                                       ct.DOMAINS['sina'])) as resp:
            lines = resp.read()
        html = lxml.html.document_fromstring(lines)
        res = html.xpath('//ul[@class=\"list_05\"]/li')
        heads = html.xpath('//div[@class=\"tit_04\"]')
        data = []
        for head in heads[:1]:
            title = head.xpath('a/text()')[0]
            url = head.xpath('a/@href')[0]
            ds = [title]
            ds.extend(_guba_content(url))
            data.append(ds)
        for row in res:
            title = row.xpath('a[2]/text()')[0]
            url = row.xpath('a[2]/@href')[0]
            ds = [title]
            ds.extend(_guba_content(url))
            data.append(ds)
        df = pd.DataFrame(data, columns=nv.GUBA_SINA_COLS)
        df['rcounts'] = df['rcounts'].astype(float)
        return df if show_content is True else df.drop('content', axis=1)
    except Exception as er:
        print(str(er))  
    
    
def _guba_content(url):
    try:
        html = lxml.html.parse(url)
        res = html.xpath('//div[@class=\"ilt_p\"]/p')
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr).replace('&#12288;', '')#.replace('\n\n', '\n').
        html_content = lxml.html.fromstring(sarr)
        content = html_content.text_content()
        ptime = html.xpath('//div[@class=\"fl_left iltp_time\"]/span/text()')[0]
        rcounts = html.xpath('//div[@class=\"fl_right iltp_span\"]/span[2]/text()')[0]
        reg = re.compile(r'\((.*?)\)') 
        rcounts = reg.findall(rcounts)[0]
        return [content, ptime, rcounts]
    except Exception:
        return ['', '', '0']


def _random(n=16):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


def get_stock_information(code, num=40):
    '''
    个股资讯

    来源: http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sz000001&Page=1
    Parameters
    --------
        code:股票代码
        num:条数
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        date:公告日期
        url:信息内容URL
    '''
    symbol = 'sh' + code if code[:1] == '6' else 'sz' + code
    data = []
    page = 1
    while 1:
        url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=%s&Page=%s' % (symbol, page)
        res = lxml.html.parse(url).xpath('//div[@class=\"datelist\"]/ul')
        if res:
            td = res[0]
            date = [d.replace(u'\xa0', ' ').strip() for d in td.xpath('text()') if d.strip()]
            title = td.xpath('a/text()')
            url = td.xpath('a/@href')
            data.extend(zip(date, title, url))
            if len(data) >= num:
                data = data[:num]
                break
        else:
            break
        page += 1
    df = pd.DataFrame(data, columns=['date', 'title', 'url'])
    return df

def get_industry_information(code, num=40):
    '''
    行业资讯

    来源: http://vip.stock.finance.sina.com.cn/corp/view/stockIndustryNews.php?symbol=sz000001&Page=1
    Parameters
    --------
        code:股票代码
        num:条数
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        date:公告日期
        url:信息内容URL
    '''
    symbol = 'sh' + code if code[:1] == '6' else 'sz' + code
    data = []
    page = 1
    while 1:
        url = 'http://vip.stock.finance.sina.com.cn/corp/view/stockIndustryNews.php?symbol=%s&Page=%s' % (symbol, page)
        res = lxml.html.parse(url).xpath('//div[@class=\"datelist\"]/ul')
        if res:
            td = res[0]
            date = [d.replace(u'\xa0', ' ').strip() for d in td.xpath('text()') if d.strip()]
            title = td.xpath('a/text()')
            url = td.xpath('a/@href')
            data.extend(zip(date, title, url))
            if len(data) >= num:
                data = data[:num]
                break
        else:
            break
        page += 1
    df = pd.DataFrame(data, columns=['date', 'title', 'url'])
    return df

def get_financial_planner_unscramble(code, num=None):
    '''
    理财师解读

    来源: http://vip.stock.finance.sina.com.cn/corp/view/vCB_FinManDiv.php?symbol=sz000001
    Parameters
    --------
        code:股票代码
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        date:公告日期
        url:信息内容URL
        name:作者名称
        author_url:作者url
    '''
    symbol = 'sh' + code if code[:1] == '6' else 'sz' + code
    data = []
    url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_FinManDiv.php?symbol=%s' % (symbol)
    res = lxml.html.parse(url).xpath('//div[@class=\"datelist\"]/ul')
    if res:
        td = res[0]
        date = [d.replace(u'\xa0', ' ').strip() for d in td.xpath('text()') if d.strip()]
        title = td.xpath('a/text()')
        url = td.xpath('a/@href')
        data.extend(zip(date[0::2], title[1::2], url[1::2], title[0::2], url[0::2]))
    df = pd.DataFrame(data, columns=['date', 'title', 'url', 'name', 'author_url'])
    return df

def get_research_report(code, num=40):
    '''
    研究报告
    来源: http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol=000001&p=1
    Parameters
    --------
        code:股票代码
        num:条数
    Return
    --------
        DataFrame，属性列表：
        title:信息标题
        date:公告日期
        url:信息内容URL
        type:类型
        institution:机构
        institution_url:机构url
        researcher:研究员
    '''
    symbol = code
    data = []
    page = 1
    while 1:
        url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol=%s&p=%s' % (symbol, page)
        res = lxml.html.parse(url).xpath('//table[@class=\"tb_01\"]/tr')
        if res:
            aNum = len(data)
            for td in res:
                dl = td.xpath('td')
                if len(dl) == 6:
                    date = dl[3].xpath('text()')[0]
                    title = dl[1].xpath('a/text()')[0].strip()
                    url = dl[1].xpath('a/@href')[0]
                    types = dl[2].xpath('text()')[0]
                    institution = dl[4].xpath('a/div/span/text()')[0]
                    institution_url = dl[4].xpath('a/@href')[0]
                    researcher = dl[5].xpath('div/span/text()')[0]
                    data.append([date, title, url, types, institution, institution_url, researcher])
            if len(data) >= num or aNum == len(data):
                data = data[:num]
                break
        else:
            break
        page += 1
    df = pd.DataFrame(data, columns=['date', 'title', 'url', 'type', 'institution', 'institution_url', 'researcher'])
    return df

def get_user_discuss(code, num=40):
    '''
    网友讨论
    来源: http://guba.sina.com.cn/?s=bar&name=sz000001&type=0&page=1
    Parameters
    --------
        code:股票代码
        num:条数
    Return
    --------
        DataFrame，属性列表：
        date:发表日期
        title:信息标题
        url:信息内容URL
        hits:点击量
        reply:回复数
        author:作者
        author_url:作者url(可空)
    '''
    symbol = 'sh' + code if code[:1] == '6' else 'sz' + code
    data = []
    page = 1
    while 1:
        url = 'http://guba.sina.com.cn/?s=bar&name=%s&type=0&page=%s' % (symbol, page)
        res = lxml.html.document_fromstring(urlopen(url).read()).xpath('//div[@id="blk_list_02"]/table/tbody/tr')
        if res:
            aNum = len(data)
            for td in res:
                dl = td.xpath('td')
                if len(dl) == 5:
                    date = dl[4].xpath('text()')[0]
                    title = dl[2].xpath('a/text()')[0].strip()
                    url = 'http://guba.sina.com.cn' + dl[2].xpath('a/@href')[0]
                    hits = dl[0].xpath('span/text()')[0]
                    reply = dl[1].xpath('span/text()')[0]
                    x = dl[3].xpath('div/a')
                    if x:
                        author, author_url = x[0].xpath('text()')[0], 'http://guba.sina.com.cn' + x[0].xpath('@href')[0]
                    else:
                        author, author_url = dl[3].xpath('div/text()')[0], None
                    data.append([date, title, url, hits, reply, author, author_url])
            if len(data) >= num or aNum == len(data):
                data = data[:num]
                break
        else:
            break
        page += 1
    df = pd.DataFrame(data, columns=['date', 'title', 'url', 'hits', 'reply', 'author', 'author_url'])
    return df
