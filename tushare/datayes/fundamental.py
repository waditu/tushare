# -*- coding:utf-8 -*- 
"""
通联数据
Created on 2015/08/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

from pandas.compat import StringIO
import pandas as pd
from tushare.util import vars as vs
from tushare.util.common import Client
from tushare.util import upass as up

class Fundamental():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
        
        
    def FdmtBS(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
               publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的合并资产负债表模板，收集了2007年以来沪深上市公司定期报告中各个会计期间的资产负债表数据；
         2、仅收集合并报表数据，包括期末和期初数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTBS%(reportType, secID, ticker, 
                                                      beginDate, endDate, publishDateBegin, 
                                                      publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtBSBank(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的银行业资产负债表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的资产负债表数据；（主要是银行业上市公司）
         2、仅收集合并报表数据，包括期末和期初数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTBSBANK%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtBSSecu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的证券业资产负债表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的资产负债表数据；（主要是证券业上市公司）
         2、仅收集合并报表数据，包括期末和期初数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTBSSECU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, 
                                                          publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtBSIndu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
             1、根据2007年新会计准则制定的一般工商业资产负债表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的资产负债表数据；（主要是一般工商业上市公司）
             2、仅收集合并报表数据，包括期末和期初数据；
             3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
             4、本表中单位为人民币元；
             5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTBSINDU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtBSInsu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的保险业资产负债表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的资产负债表数据；（主要是保险业上市公司）
         2、仅收集合并报表数据，包括期末和期初数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元。
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTBSINSU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtCF(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
               publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的合并现金流量表模板，收集了2007年以来沪深上市公司定期报告中各个会计期间的现金流量表数据；
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTCF%(reportType, secID, ticker, 
                                                      beginDate, endDate, 
                                                      publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtCFBank(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
            1、根据2007年新会计准则制定的银行业现金流量表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的现金流量表数据；（主要是银行业上市公司） 2、仅收集合并报表数据，包括本期和上期数据； 3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示； 4、本表中单位为人民币元；5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTCFBANK%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtCFSecu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
            1、根据2007年新会计准则制定的证券业现金流量表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的现金流量表数据；（主要是证券业上市公司） 
            2、仅收集合并报表数据，包括本期和上期数据； 
            3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示； 
            4、本表中单位为人民币元；
            5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTCFSECU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtCFIndu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的一般工商业现金流量表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的现金流量表数据；（主要是一般工商业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTCFINDU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtCFInsu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的保险业现金流量表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的现金流量表数据；（主要是保险业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTCFINSU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtIS(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
               publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的合并利润表模板，收集了2007年以来沪深上市公司定期报告中各个会计期间的利润表数据；
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTIS%(reportType, secID, ticker, 
                                                      beginDate, endDate, 
                                                      publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtISBank(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的银行业利润表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的利润表数据；（主要是银行业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTISBANK%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtISSecu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的证券业利润表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的利润表数据；（主要是证券业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTISSECU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)
    

    def FdmtISIndu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的一般工商业利润表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的利润表数据；（主要是一般工商业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTISINDU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)
    

    def FdmtISInsu(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
                   publishDateBegin='', publishDateEnd='', field=''):
        """
         1、根据2007年新会计准则制定的保险业利润表模板，收集了2007年以来沪深上市公司定期报告中所有以此模板披露的利润表数据；（主要是保险业上市公司）
         2、仅收集合并报表数据，包括本期和上期数据；
         3、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
         4、本表中单位为人民币元；
         5、每季更新。
        """
        code, result = self.client.getData(vs.FDMTISINSU%(reportType, secID, ticker, 
                                                          beginDate, endDate, 
                                                          publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtEe(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
               publishDateBegin='', publishDateEnd='', field=''):
        """
            获取2007年及以后年度上市公司披露的业绩快报中的主要财务指标等其他数据，
            包括本期，去年同期，及本期与期初数值同比数据。每季证券交易所披露相关公告时更新数据，
            公司ipo时发布相关信息也会同时更新。每日9：00前完成证券交易所披露的数据更新，中午发布公告每日12：45前完成更新。
        """
        code, result = self.client.getData(vs.FDMTEE%(reportType, secID, ticker, 
                                                      beginDate, endDate, 
                                                      publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtEf(self, reportType='', secID='', ticker='', beginDate='', endDate='', 
               forecastType='', publishDateBegin='', publishDateEnd='', field=''):
        """
            1、获取2007年及以后年度上市公司披露的公告中的预期下一报告期收入、净利润、归属于母公司净利润、基本每股收益及其幅度变化数据。
            2、上市公司对经营成果科目的预计情况数据一般为其上限与下限，上限取值为公告中披露该科目中绝对值较大值，下限取值为公告中披露该科目中绝对值较小值。
            3、数值为"正"代表该公司预计盈利，数值为"负"代表该公司预计亏损。若上下限"正"、"负"符号不同，代表该公司盈利亏损情况尚不确定。
            4、业绩预期类型以公告中文字披露预期类型为准，若公告中未有文字披露预期类型，则根据数据情况判断预期类型。
            5、每季证券交易所披露相关公告时更新数据，公司ipo时发布相关信息也会同时更新。每日9：00前完成证券交易所披露的数据更新，中午发布公告每日12：45前完成更新。
        """
        code, result = self.client.getData(vs.FDMTEF%(reportType, secID, ticker, 
                                                      beginDate, endDate, forecastType, 
                                                      publishDateBegin, publishDateEnd, field))
        return _ret_data(code, result)


    def FdmtISLately(self, field=''):
        """
            1、可获取上市公司最近一次数据，根据2007年新会计准则制定的合并利润表模板，仅收集合并报表数据；
            2、如果上市公司对外财务报表进行更正，调整，均有采集并对外展示；
            3、本表中单位为人民币元；
            4、每季更新。
        """
        code, result = self.client.getData(vs.FDMTISLATELY%(field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
