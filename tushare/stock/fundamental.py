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
import re

def get_stock_basics(file_path=ct.ALL_STOCK_BASICS_FILE):
    """
        获取沪深上市公司基本情况
    Parameters
    --------
    file_path:a file path string,default as 'data/all.csv' in the package
        you can use your own file with the same columns 
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
    df = pd.read_csv(file_path,dtype={'code':'object'},encoding='GBK')
    df = df.set_index('code')
    return df

def get_report_data(year,quarter):
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
    if _check_input(year,quarter) is True:
        data =  _get_report_data(year,quarter,1,[])
        df = pd.DataFrame(data,columns=ct.REPORT_COLS)
        return df

def _get_report_data(year,quarter,pageNo,dataArr):
    url = ct.REPORT_URL%(ct.P_TYPE['http'],ct.DOMAINS['sina'],year,quarter,pageNo)
    print 'getting page %s ...'%pageNo
    try:
        html = lxml.html.parse(url)
        xtrs = html.xpath("//table[@class=\"list_table\"]/tr")
        for trs in xtrs:
            code = trs.xpath('td[1]//span/a/text()')[0]
            name = trs.xpath('td[2]/span/a/text()')[0]
            eps = trs.xpath('td[3]/text()')[0] #每股收益(元)
            eps_yoy = trs.xpath('td[4]/text()')[0] #每股收益同比(%)
            bvps = trs.xpath('td[5]/text()')[0] #每股净资产(元)
            bvps = '0' if bvps == '--' else bvps
            roe = trs.xpath('td[6]/text()')[0] #净资产收益率(%)
            roe = '0' if roe == '--' else roe
            epcf = trs.xpath('td[7]/text()')[0] #每股现金流量(元)
            epcf = '0' if epcf == '--' else epcf
            net_profits = trs.xpath('td[8]/text()')[0] #净利润(万元)
            profits_yoy = trs.xpath('td[9]/text()')[0] #净利润同比(%)
            distrib = trs.xpath('td[10]/text()')[0] #分配方案
            report_date = trs.xpath('td[11]/text()')[0] #发布日期
            dataArr.append([code,name,eps,eps_yoy,bvps,roe,epcf,net_profits,profits_yoy,distrib,report_date])
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick') #获取下一页
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_report_data(year,quarter,pageNo,dataArr)
        else:
            return dataArr
    except:
        pass

def get_forecast_data(year,quarter):
    """
        获取业绩预告数据
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
        type,业绩变动类型
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
    """
    if _check_input(year,quarter) is True:
        data =  _get_forecast_data(year,quarter,1,[])
        df = pd.DataFrame(data,columns=ct.FORECAST_COLS)
        return df

def _get_forecast_data(year,quarter,pageNo,dataArr):
    url = ct.FORECAST_URL%(ct.P_TYPE['http'],ct.DOMAINS['sina'],year,quarter,pageNo)
    print 'getting page %s ...'%pageNo
    try:
        html = lxml.html.parse(url)
        xtrs = html.xpath("//table[@class=\"list_table\"]/tr")
        for trs in xtrs:
            code = trs.xpath('td[1]//span/a/text()')[0]
            name = trs.xpath('td[2]/span/a/text()')[0]
            type = trs.xpath('td[3]/a/text()')
            type = type[0] if len(type)>0 else trs.xpath('td[3]/text()')[0]
            report_date = trs.xpath('td[4]/text()')[0] 
            pre_eps = trs.xpath('td[7]/text()')[0] 
            pre_eps = '0' if pre_eps == '--' else pre_eps
            range = trs.xpath('td[8]/text()')[0] 
            dataArr.append([code,name,type,report_date,pre_eps,range])
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick') #获取下一页
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_forecast_data(year,quarter,pageNo,dataArr)
        else:
            return dataArr
    except:
        pass

def get_profit_data(year,quarter):
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
    if _check_input(year,quarter) is True:
        data =  _get_profit_data(year,quarter,1,[])
        df = pd.DataFrame(data,columns=ct.PROFIT_COLS)
        return df

def _get_profit_data(year,quarter,pageNo,dataArr):
    url = ct.PROFIT_URL%(ct.P_TYPE['http'],ct.DOMAINS['sina'],year,quarter,pageNo)
    print 'getting page %s ...'%pageNo
    try:
        html = lxml.html.parse(url)
        xtrs = html.xpath("//table[@class=\"list_table\"]/tr")
        for trs in xtrs:
            code = trs.xpath('td[1]/a/text()')[0]
            name = trs.xpath('td[2]/a/text()')[0]
            roe = trs.xpath('td[3]/text()')[0]
            roe = '0' if roe == '--' else roe
            net_profit_ratio = trs.xpath('td[4]/text()')[0] 
            net_profit_ratio = '0' if net_profit_ratio == '--' else net_profit_ratio
            gross_profit_rate = trs.xpath('td[5]/text()')[0] 
            gross_profit_rate = '0' if gross_profit_rate == '--' else gross_profit_rate
            net_profits = trs.xpath('td[6]/text()')[0] 
            net_profits = '0' if net_profits == '--' else net_profits
            eps = trs.xpath('td[7]/text()')[0] 
            eps = '0' if eps == '--' else eps
            business_income = trs.xpath('td[8]/text()')[0] 
            business_income = '0' if business_income == '--' else business_income
            bips = trs.xpath('td[9]/text()')[0] 
            bips = '0' if bips == '--' else bips
            dataArr.append([code,name,roe,net_profit_ratio,gross_profit_rate,net_profits,eps,business_income,bips])
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick') #获取下一页
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_profit_data(year,quarter,pageNo,dataArr)
        else:
            return dataArr
    except:
        pass

def get_operation_data(year,quarter):
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
    if _check_input(year,quarter) is True:
        data =  _get_operation_data(year,quarter,1,[])
        df = pd.DataFrame(data,columns=ct.OPERATION_COLS)
        return df

def _get_operation_data(year,quarter,pageNo,dataArr):
    url = ct.OPERATION_URL%(ct.P_TYPE['http'],ct.DOMAINS['sina'],year,quarter,pageNo)
    print 'getting page %s ...'%pageNo
    try:
        html = lxml.html.parse(url)
        xtrs = html.xpath("//table[@class=\"list_table\"]/tr")
        for trs in xtrs:
            code = trs.xpath('td[1]/a/text()')[0]
            name = trs.xpath('td[2]/a/text()')[0]
            arturnover = trs.xpath('td[3]/text()')[0]
            arturnover = '0' if arturnover == '--' else arturnover
            arturndays = trs.xpath('td[4]/text()')[0] 
            arturndays = '0' if arturndays == '--' else arturndays
            inventory_turnover = trs.xpath('td[5]/text()')[0] 
            inventory_turnover = '0' if inventory_turnover == '--' else inventory_turnover
            inventory_days = trs.xpath('td[6]/text()')[0] 
            inventory_days = '0' if inventory_days == '--' else inventory_days
            currentasset_turnover = trs.xpath('td[7]/text()')[0] 
            currentasset_turnover = '0' if currentasset_turnover == '--' else currentasset_turnover
            currentasset_days = trs.xpath('td[8]/text()')[0] 
            currentasset_days = '0' if currentasset_days == '--' else currentasset_days
            dataArr.append([code, name,arturnover,arturndays,inventory_turnover,inventory_days,currentasset_turnover,currentasset_days])
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick') #获取下一页
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+',nextPage[0])[0]
            return _get_operation_data(year,quarter,pageNo,dataArr)
        else:
            return dataArr
    except:
        pass
    
def _check_input(year,quarter):
    if type(year) is str or year < 1989 :
        raise TypeError('年度输入错误：请输入1989年以后的年份数字，格式：YYYY')
    elif quarter is None or type(quarter) is str or quarter not in [1,2,3,4]:
        raise TypeError('季度输入错误：请输入1、2、3或4数字')
    else:
        return True

if __name__ == '__main__':
#     print get_report_data(2013,4)
#     print get_profit_data(1999,2)
    print get_operation_data(1999,2)
#     print get_stock_basics()

    