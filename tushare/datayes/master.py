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

class Master():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def SecID(self, assetClass='', cnSpell='', partyID='', ticker='', field=''):
        """
            通过机构partyID,或证券简称拼音cnSpell,或证券交易代码ticker，
            检索证券ID（证券在数据结构中的一个唯一识别的编码），
            也可通过证券简称拼音cnSpell检索证券交易代码ticker等；同时可以获取输入证券的基本上市信息，如交易市场，上市状态，交易币种，ISIN编码等。
        """
        code, result = self.client.getData(vs.SECID%(assetClass, cnSpell, partyID, ticker, field))
        return _ret_data(code, result)
    

    def TradeCal(self, exchangeCD='', beginDate='', endDate='', field=''):
        """
            记录了上海证券交易所,深圳证券交易所,中国银行间市场,大连商品交易所,郑州商品交易所,上海期货交易所,
            中国金融期货交易所和香港交易所等交易所在日历日期当天是否开市的信息，
            其中上证、深证记录了自成立以来的全部日期是否开始信息。各交易日节假日安排通知发布当天即更新数据。
        """
        code, result = self.client.getData(vs.TRADECAL%(exchangeCD, beginDate, endDate, field))
        return _ret_data(code, result)


    def Industry(self, industryVersion='', industryVersionCD='', industryLevel='', isNew='', field=''):
        """
            输入行业分类通联编码(如，010303表示申万行业分类2014版)或输入一个行业分类标准名称，获取行业分类标准下行业划分
        """
        code, result = self.client.getData(vs.INDUSTRY%(industryVersion, industryVersionCD,
                                                        industryLevel, isNew, field))
        return _ret_data(code, result)


    def SecTypeRel(self, secID='', ticker='', typeID='', field=''):
        """
            记录证券每个分类的成分，证券分类可通过在getSecType获取。
        """
        code, result = self.client.getData(vs.SECTYPEREL%(secID, ticker, typeID, field))
        return _ret_data(code, result)


    def EquInfo(self, ticker='', field=''):
        """
            根据拼音或股票代码，匹配股票代码、名称。包含正在上市的全部沪深股票。
        """
        code, result = self.client.getData(vs.EQUINFO%(ticker, field))
        return _ret_data(code, result)


    def SecTypeRegionRel(self, secID='', ticker='', typeID='', field=''):
        """
            获取沪深股票地域分类，以注册地所在行政区域为标准。
        """
        code, result = self.client.getData(vs.SECTYPEREGIONREL%(secID, ticker, typeID, field))
        return _ret_data(code, result)


    def SecType(self, field=''):
        """
            证券分类列表，一级分类包含有沪深股票、港股、基金、债券、期货、期权等，每个分类又细分有不同类型；可一次获取全部分类。
        """
        code, result = self.client.getData(vs.SECTYPE%(field))
        return _ret_data(code, result)


    def SecTypeRegion(self, field=''):
        """
            获取中国地域分类，以行政划分为标准。
        """
        code, result = self.client.getData(vs.SECTYPEREGION%(field))
        return _ret_data(code, result)


    def SysCode(self, codeTypeID='', valueCD='', field=''):
        """
            各api接口有枚举值特性的输出列，如getSecID输出项exchangeCD值，编码分别代表的是什么市场，所有枚举值都可以在这个接口获取。
        """
        code, result = self.client.getData(vs.SYSCODE%(codeTypeID, valueCD, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    