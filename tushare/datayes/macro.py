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

class Macro():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
    def ChinaMacroData(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国宏观主要指标数据，历史数据从1928年开始。具体指标请查询“中国宏观指标”API。
        """
        code, result = self.client.getData(vs.CHINAMACRODATA%(indicID, indicName, 
                                                              beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaMacroInfo(self, indicID='', indicNameAbbr='', parentID='', field=''):
        """
            包含中国宏观指标信息。输入中国宏观指标代码或名称，查询具体指标信息，如：指标频度、单位、来源等。
        """
        code, result = self.client.getData(vs.CHINAMACROINFO%(indicID, indicNameAbbr, parentID, field))
        return _ret_data(code, result)


    def GlobalMacroData(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含全球宏观20多个主要国家地区重要宏观指标数据，历史数据从1900年开始。具体指标请查询“全球宏观指标”API。
        """
        code, result = self.client.getData(vs.GLOBALMACRODATA%(indicID, indicName,
                                                                beginDate, endDate, field))
        return _ret_data(code, result)


    def GlobalMacroInfo(self, indicID='', indicNameAbbr='', parentID='', field=''):
        """
            包含全球宏观指标信息。输入全球宏观指标代码或名称，查询具体指标信息，如，指标频度、单位、来源等。
        """
        code, result = self.client.getData(vs.GLOBALMACROINFO%(indicID, indicNameAbbr, parentID, field))
        return _ret_data(code, result)


    def IndustrialData(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含行业主要指标数据，历史数据从1947年开始。具体指标请查询“行业经济指标”API。
        """
        code, result = self.client.getData(vs.INDUSTRIALDATA%(indicID, indicName, 
                                                              beginDate, endDate, field))
        return _ret_data(code, result)


    def IndustrialInfo(self, indicID='', indicNameAbbr='', parentID='', field=''):
        """
            包含行业指标信息。输入行业经济指标代码或名称，查询具体指标信息，如，指标频度、单位、来源等。
        """
        code, result = self.client.getData(vs.INDUSTRIALINFO%(indicID, indicNameAbbr, parentID, field))
        return _ret_data(code, result)


    def EcommerceData(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含电商指标数据，历史数据从2014年8月开始。具体指标请查询“电商指标”API。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def EcommerceInfo(self, indicID='', indicNameAbbr='', parentID='', field=''):
        """
            包含电商指标信息。输入电商指标代码或名称，查询具体指标信息，如，指标频度、单位、来源等。
        """
        code, result = self.client.getData(vs.ECOMMERCEINFO%(indicID, indicNameAbbr, parentID, field))
        return _ret_data(code, result)


    def ChinaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国GDP数据，具体指标可参见API文档；历史数据从1984年开始，按季更新。
        """
        code, result = self.client.getData(vs.CHINADATAGDP%(indicID, indicName, 
                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataECI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国宏观经济景气指数数据，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAECI%(indicID, indicName, 
                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataPMI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国PMI、汇丰中国PMI数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAPMI%(indicID, indicName, 
                                                            beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataCCI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国消费者景气指数数据，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATACCI%(indicID, indicName, 
                                                            beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataEconomistsBoomIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国经济学家景气指数数据，具体指标可参见API文档；历史数据从2006年开始，按季更新。
        """
        code, result = self.client.getData(vs.CHINADATAECONOMISTSBOOMINDEX%(indicID, indicName, 
                                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataIndustrialBusinessClimateIndex(self, indicID='', indicName='', 
                                                beginDate='', endDate='', field=''):
        """
            包含中国工业景气指数数据，具体指标可参见API文档；历史数据从1999年开始，按季更新。
        """
        code, result = self.client.getData(vs.CHINADATAINDUSTRIALBUSINESSCLIMATEINDEX%(indicID, indicName, 
                                                                                       beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国居民消费价格指数(CPI)数据,，含36大中城市CPI数据，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataPPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国工业价格指数数据，如PPI、分行业PPI、PPIRM，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAPPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国工业数据，如工业生产运行、工业企业主要经济指标，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataRetailSales(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国社会消费品零售数据，具体指标可参见API文档；历史数据从1984年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATARETAILSALES%(indicID, indicName, 
                                                                    beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataResidentIncomeExp(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国城镇、农村居民家庭收支数据，具体指标可参见API文档；历史数据从1984年开始，按季更新。
        """
        code, result = self.client.getData(vs.CHINADATARESIDENTINCOMEEXP%(indicID, indicName, 
                                                                          beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataFAI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国固定资产投资数据，如投资额、资金来源、分行业投资，具体指标可参见API文档；历史数据从1990年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAFAI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国房地产开发数据，如房地产景气指数、投资额、来源、商品房销售、土地开发购置，具体指标可参见API文档；历史数据从1991年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国进出口数据，具体指标可参见API文档；历史数据从1990年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAFOREIGNTRADE%(indicID, indicName, 
                                                                     beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataFDI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国外商直接投资数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAFDI%(indicID, indicName, 
                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataMoneyStatistics(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国货币统计数据，如货币供应、黄金外汇储备，具体指标可参见API文档；历史数据从1951年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAMONEYSTATISTICS%(indicID, indicName, 
                                                                        beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataAllSystemFinancing(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国社会融资规模数据，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAALLSYSTEMFINANCING%(indicID, indicName, 
                                                                           beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataLendingDeposit(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国金融机构存贷款数据，具体指标可参见API文档；历史数据从1978年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATALENDINGDEPOSIT%(indicID, indicName, 
                                                                       beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataCreditFundsTable(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国金融机构信贷收支表数据，具体指标可参见API文档；历史数据从1952年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATACREDITFUNDSTABLE%(indicID, indicName, 
                                                                         beginDate, endDate, field))
        return _ret_data(code, result)
    

    def ChinaDataOpenMarketOperation(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国人民银行公开市场回购数据，如正回购、逆回购，具体指标可参见API文档；历史数据从1952年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAOPENMARKETOPERATION%(indicID, indicName, 
                                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国人民币汇率数据，如人民币汇率中间价、人民币汇率指数，具体指标可参见API文档；历史数据从1994年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.CHINADATAEXCHANGERATE%(indicID, indicName, 
                                                                     beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataInterestRateLendingDeposit(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国官方发布的存贷款利率数据，具体指标可参见API文档；历史数据从1949年8月开始，按日更新。
        """
        code, result = self.client.getData(vs.CHINADATAINTERESTRATELENDINGDEPOSIT%(indicID, indicName, 
                                                                                   beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataInterestRateSHIBOR(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国银行间同业拆借(Shibor)数据，具体指标可参见API文档；历史数据从2006年10月开始，按日更新。
        """
        code, result = self.client.getData(vs.CHINADATAINTERESTRATESHIBOR%(indicID, indicName,
                                                                            beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataInterestRateInterbankRepo(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国银行间同业拆借数据，如质押式回购、买断式回购，具体指标可参见API文档；历史数据从2005年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.CHINADATAINTERESTRATEINTERBANKREPO%(indicID, indicName, 
                                                                                  beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国财政数据，如全国财政收支、各省及直辖市财政收入，具体指标可参见API文档；历史数据从1990年开始，按月更新。
        """
        code, result = self.client.getData(vs.CHINADATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def ChinaDataGoldClosePrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含中国上海黄金收盘价数据，具体指标可参见API文档；历史数据从2004年9月开始，按日更新。
        """
        code, result = self.client.getData(vs.CHINADATAGOLDCLOSEPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国GDP数据，具体指标可参见API文档；历史数据从1947年开始，按季更新。
        """
        code, result = self.client.getData(vs.USDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国对外贸易数据，具体指标可参见API文档；历史数据从1992年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国价格指数数据，如CPI、PPI、进出口价格指数，具体指标可参见API文档；历史数据从1913年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataEmploymentUnemployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国就业与失业数据，如非农就业、ADP就业报告，具体指标可参见API文档；历史数据从1939年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATAEMPLOYMENTUNEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataInterestRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国利率数据，如联邦基金利率、国债收益率、Libor美元，具体指标可参见API文档；历史数据从1954年7月开始，按日更新。
        """
        code, result = self.client.getData(vs.USDATAINTERESTRATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国汇率数据，如美元对主要货币、美元指数，具体指标可参见API文档；历史数据从1973年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.USDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国货币供应量数据，具体指标可参见API文档；历史数据从1959年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataConsumerCredit(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国消费信贷数据，具体指标可参见API文档；历史数据从1943年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATACONSUMERCREDIT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国景气指数数据，如PMI、消费者信息指数、ECRI领先指标，具体指标可参见API文档；历史数据从1948年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataDurableGoods(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国工业中耐用品数据，具体指标可参见API文档；历史数据从1992年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATADURABLEGOODS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国房地产数据，具体指标可参见API文档；历史数据从1959年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def USDataDomesticTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国国内贸易数据，具体指标可参见API文档；历史数据从1992年开始，按月更新。
        """
        code, result = self.client.getData(vs.USDATADOMESTICTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟GDP数据，具体指标可参见API文档；历史数据从1995年开始，按季更新。
        """
        code, result = self.client.getData(vs.EUDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟对外贸易数据，具体指标可参见API文档；历史数据从2013年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟价格指数数据，如CPI、PPI、单位进出口价格指数，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataEmploymentUnemployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟就业与失业数据，如就业失业率、劳动力成本指数，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATAEMPLOYMENTUNEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataInterestRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟利率数据，如Libor、政府债券收益率、欧元区公债收益率，具体指标可参见API文档；历史数据从1980年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.EUDATAINTERESTRATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟汇率数据，具体指标可参见API文档；历史数据从1999年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.EUDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟金融数据，如货币供应、官方储备资产，具体指标可参见API文档；历史数据从1980年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟景气指数数据，如PMI、经济景气指数、消费者信息指数，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟工业数据，如营建产出、供应生产指数，具体指标可参见API文档；历史数据从2013年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EUDataRetail(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含欧盟零售销售数据，具体指标可参见API文档；历史数据从2013年开始，按月更新。
        """
        code, result = self.client.getData(vs.EUDATARETAIL%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwitzerlandDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞士GDP数据，具体指标可参见API文档；历史数据从1980年开始，按季更新。
        """
        code, result = self.client.getData(vs.SWITZERLANDDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwitzerlandDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞士价格指数数据，如CPI、PPI，具体指标可参见API文档；历史数据从1922年开始，按月更新。
        """
        code, result = self.client.getData(vs.SWITZERLANDDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwitzerlandDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞士SVME采购经理人指数数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.SWITZERLANDDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwitzerlandDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞士货币供应量数据，具体指标可参见API文档；历史数据从1975年开始，按月更新。
        """
        code, result = self.client.getData(vs.SWITZERLANDDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwedenDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞典GDP数据，具体指标可参见API文档；历史数据从1993年开始，按季更新。
        """
        code, result = self.client.getData(vs.SWEDENDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwedenDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞典价格指数数据，如CPI、PPI、进出口价格指数，具体指标可参见API文档；历史数据从1980年开始，按月更新。
        """
        code, result = self.client.getData(vs.SWEDENDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SwedenDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含瑞典对外贸易数据，具体指标可参见API文档；历史数据从1975年开始，按月更新。
        """
        code, result = self.client.getData(vs.SWEDENDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国GDP数据，具体指标可参见API文档；历史数据从1970年开始，按季更新。
        """
        code, result = self.client.getData(vs.KOREADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国价格指数数据，具体指标可参见API文档；历史数据从1965年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataEmploymentUnemployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国就业与失业数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATAEMPLOYMENTUNEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国利率数据，具体指标可参见API文档；历史数据从1995年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.KOREADATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国汇率数据，具体指标可参见API文档；历史数据从1964年5月开始，按日更新。
        """
        code, result = self.client.getData(vs.KOREADATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国货币供应量数据，具体指标可参见API文档；历史数据从1970年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国景气指数数据，如企业景气调查指数、消费者调查指数、PMI、消费者信心指数，具体指标可参见API文档；历史数据从2008年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaData_ExternalDebt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国外债数据，具体指标可参见API文档；历史数据从1994年开始，按季更新。
        """
        code, result = self.client.getData(vs.KOREADATA_EXTERNALDEBT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataIndustryandService(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国工业与服务业数据，如工业指数、制造业指数、服务业活动指数，具体指标可参见API文档；历史数据从1970年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATAINDUSTRYANDSERVICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def KoreaDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含韩国房地产数据，具体指标可参见API文档；历史数据从1987年开始，按月更新。
        """
        code, result = self.client.getData(vs.KOREADATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AustraliaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳大利亚GDP数据，具体指标可参见API文档；历史数据从1959年开始，按季更新。
        """
        code, result = self.client.getData(vs.AUSTRALIADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AustraliaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳大利亚贸易数据，如对外贸易、零售销售，具体指标可参见API文档；历史数据从1971年开始，按月更新。
        """
        code, result = self.client.getData(vs.AUSTRALIADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AustraliaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳大利亚价格指数数据，如消费者物价指数数据(CPI)、生产价格指数数据(PPI)，具体指标可参见API文档；历史数据从1948年开始，按季更新。
        """
        code, result = self.client.getData(vs.AUSTRALIADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AustraliaDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳大利亚就业和工资数据，如就业、ANZ总招聘广告，具体指标可参见API文档；历史数据从1978年开始，按月更新。
        """
        code, result = self.client.getData(vs.AUSTRALIADATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AustraliaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳大利亚景气调查数据，如消费者信心指数、PMI、PSC、PCI，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.AUSTRALIADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利国内生产总值(GDP)数据，具体指标可参见API文档；历史数据从1992年开始，按季更新。
        """
        code, result = self.client.getData(vs.ITALYDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利国际收支数据，具体指标可参见API文档；历史数据从1970年开始，按季更新。
        """
        code, result = self.client.getData(vs.ITALYDATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利价格指数数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.ITALYDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利就业和工资数据，如就业、工资，具体指标可参见API文档；历史数据从1983年开始，按月更新。
        """
        code, result = self.client.getData(vs.ITALYDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利财政数据，具体指标可参见API文档；历史数据从1995年开始，按年更新。
        """
        code, result = self.client.getData(vs.ITALYDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利景气调查数据，具体指标可参见API文档；历史数据从1985年开始，按月更新。
        """
        code, result = self.client.getData(vs.ITALYDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ItalyDataInterestRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含意大利利率数据，具体指标可参见API文档；历史数据从1980年开始，按月更新。
        """
        code, result = self.client.getData(vs.ITALYDATAINTERESTRATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙GDP数据，具体指标可参见API文档；历史数据从1960年开始，按季更新。
        """
        code, result = self.client.getData(vs.SPAINDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙对外贸易数据，具体指标可参见API文档；历史数据从1960年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙国际收支数据，具体指标可参见API文档；历史数据从1980年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙金融数据，如货币供应、银行业，具体指标可参见API文档；历史数据从1960年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataTransportation(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙交通运输和电信数据，具体指标可参见API文档；历史数据从1960年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATATRANSPORTATION%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataEnergy(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙能源数据，具体指标可参见API文档；历史数据从1960年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATAENERGY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SpainDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含西班牙财政数据，具体指标可参见API文档；历史数据从1995年开始，按年更新。
        """
        code, result = self.client.getData(vs.SPAINDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大GDP数据，具体指标可参见API文档；历史数据从1962年开始，按季更新。
        """
        code, result = self.client.getData(vs.CANADADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大国际收支数据，具体指标可参见API文档；历史数据从2012年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大对外贸易数据，具体指标可参见API文档；历史数据从2008年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大价格指数数据，如CPI、生产价格指数，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大金融数据，如货币供应量、国际储备，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大就业和工资数据，如就业、平均周薪，具体指标可参见API文档；历史数据从1991年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataManufacturing(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大工业和制造业数据，具体指标可参见API文档；历史数据从2008年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAMANUFACTURING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大房地产数据，如新房屋价格指数、建设许可，具体指标可参见API文档；历史数据从2003年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CanadaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含加拿大景气调查数据，如Markit采购经理人指数、IVEY采购经理人指数，具体指标可参见API文档；历史数据从2011年开始，按月更新。
        """
        code, result = self.client.getData(vs.CANADADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港GDP数据，具体指标可参见API文档；历史数据从1973年开始，按季更新。
        """
        code, result = self.client.getData(vs.HKDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港对外贸易及投资数据，具体指标可参见API文档；历史数据从1952年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港价格指数数据，如CPI、PPI，具体指标可参见API文档；历史数据从1974年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港财政数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港金融数据，如货币金融概况、流通货币，具体指标可参见API文档；历史数据从1968年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港工业数据，具体指标可参见API文档；历史数据从2009年开始，按季更新。
        """
        code, result = self.client.getData(vs.HKDATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataConsumption(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港零售业总销货数据，具体指标可参见API文档；历史数据从2001年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATACONSUMPTION%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataThroughput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港货物吞吐量数据，具体指标可参见API文档；历史数据从2010年开始，按季更新。
        """
        code, result = self.client.getData(vs.HKDATATHROUGHPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港人口与就业数据，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataInterestRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港利率数据，如利率、银行同业拆息，具体指标可参见API文档；历史数据从1980年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.HKDATAINTERESTRATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港汇率数据，具体指标可参见API文档；历史数据从2007年7月开始，按日更新。
        """
        code, result = self.client.getData(vs.HKDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港房地产数据，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HKDataTourism(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含香港旅游业数据，如访港旅客、酒店住宿，具体指标可参见API文档；历史数据从2010年开始，按月更新。
        """
        code, result = self.client.getData(vs.HKDATATOURISM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度GDP数据，具体指标可参见API文档；历史数据从2009年开始，按季更新。
        """
        code, result = self.client.getData(vs.INDIADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度国际收支数据，如外债、国际投资寸头，具体指标可参见API文档；历史数据从2006年开始，按季更新。
        """
        code, result = self.client.getData(vs.INDIADATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度价格指数数据，如CPI、批发价格指数、房屋价格指数，具体指标可参见API文档；历史数据从1995年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataTourism(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度旅游业数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATATOURISM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataEnergy(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度能源数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATAENERGY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度景气调查数据，具体指标可参见API文档；历史数据从2012年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度金融数据，如货币供应量、对外贸易，具体指标可参见API文档；历史数据从2011年开始，按周更新。
        """
        code, result = self.client.getData(vs.INDIADATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度工业数据，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndiaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度对外贸易数据，具体指标可参见API文档；历史数据从1994年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDIADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚GDP数据，具体指标可参见API文档；历史数据从2007年开始，按季更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚国际收支数据，如国际收支、外汇准备金，具体指标可参见API文档；历史数据从1998年开始，按季更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚对外贸易数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚价格指数据，如PPI、消费者价格指数，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚就业数据，具体指标可参见API文档；历史数据从2010年开始，按月更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚工业数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚财政数据，具体指标可参见API文档；历史数据从1996年开始，按季更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚货币供应量数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MalaysiaDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含马来西亚房地产数据，具体指标可参见API文档；历史数据从2004年开始，按季更新。
        """
        code, result = self.client.getData(vs.MALAYSIADATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚GDP数据，具体指标可参见API文档；历史数据从2001年开始，按季更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚国际收支国际收支、外债数据，具体指标可参见API文档；历史数据从1996年开始，按季更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚对外贸易数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚消费者价格指数(CPI)(CPI)数据，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚工业数据，具体指标可参见API文档；历史数据从2003年开始，按年更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚财政数据，具体指标可参见API文档；历史数据从2003年开始，按季更新。
        """
        code, result = self.client.getData(vs.INDONESIADATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataBanking(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚货币供应量数据，具体指标可参见API文档；历史数据从1989年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDONESIADATABANKING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataSecurity(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚证券市场数据，如资本市场发行的股票和债券、政府未尝还投资组合，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDONESIADATASECURITY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def IndonesiaDataTourism(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含印度尼西亚旅游业数据，具体指标可参见API文档；历史数据从2008年开始，按月更新。
        """
        code, result = self.client.getData(vs.INDONESIADATATOURISM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其GDP数据，具体指标可参见API文档；历史数据从1998年开始，按季更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其国际收支数据，如国际收支、外汇储备、外债，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其对外贸易数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其价格指数数据，如CPI、PPI，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其就业数据，具体指标可参见API文档；历史数据从2012年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其工业数据，具体指标可参见API文档；历史数据从2012年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其财政数据，具体指标可参见API文档；历史数据从2006年开始，按月更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TurkeyDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含土耳其货币供应量数据，具体指标可参见API文档；历史数据从2005年开始，按周更新。
        """
        code, result = self.client.getData(vs.TURKEYDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国GDP数据，具体指标可参见API文档；历史数据从1993年开始，按季更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataPaymentsBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国国际收支数据，如国际收支、外汇储备、外债，具体指标可参见API文档；历史数据从1987年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAPAYMENTSBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国对外贸易数据，具体指标可参见API文档；历史数据从2010年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国价格指数数据，如CPI、PPI，具体指标可参见API文档；历史数据从1976年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国就业数据，如就业、劳动指数、劳动生产率指数，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国工业数据，如工业生产指数、产能利用率、出货量指数、产成品存货指数，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国财政数据，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国商业景气指数数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThailandDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含泰国货币供应量数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.THAILANDDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国GDP数据，具体指标可参见API文档；历史数据从1955年开始，按季更新。
        """
        code, result = self.client.getData(vs.UKDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国对外贸易数据，具体指标可参见API文档；历史数据从1971年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从1988年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataRPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国零售价格指数(RPI)数据，具体指标可参见API文档；历史数据从1948年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATARPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国就业数据，具体指标可参见API文档；历史数据从1971年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国货币供应量数据，具体指标可参见API文档；历史数据从1998年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataConsumerCredit(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国消费信贷数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATACONSUMERCREDIT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国景气指数数据，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国财政收支数据，具体指标可参见API文档；历史数据从1991年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataIndustrialPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国工业生产指数数据，具体指标可参见API文档；历史数据从1968年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAINDUSTRIALPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataHousePI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国房价指数数据，具体指标可参见API文档；历史数据从1983年开始，按月更新。
        """
        code, result = self.client.getData(vs.UKDATAHOUSEPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国利率数据，具体指标可参见API文档；历史数据从1975年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.UKDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UKDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含英国汇率数据，具体指标可参见API文档；历史数据从1975年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.UKDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本GDP数据，具体指标可参见API文档；历史数据从1980年开始，按季更新。
        """
        code, result = self.client.getData(vs.JAPANDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本对外贸易数据，具体指标可参见API文档；历史数据从1979年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从1970年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本就业与失业数据，具体指标可参见API文档；历史数据从1953年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本货币供应量数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本景气指数数据，如景气动向指数、消费者信心指数、PMI，具体指标可参见API文档；历史数据从1980年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataIndustrialPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本工业生产指数数据，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATAINDUSTRIALPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataHousePI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本房价指数数据，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.JAPANDATAHOUSEPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本利率数据，具体指标可参见API文档；历史数据从1998年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.JAPANDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def JapanDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含日本汇率数据，具体指标可参见API文档；历史数据从1998年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.JAPANDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国GDP数据，具体指标可参见API文档；历史数据从1991年开始，按季更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国对外贸易数据，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从1994年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataPPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国生产者价格指数(PPI)数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAPPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataImportExportPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国进出口价格指数数据，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAIMPORTEXPORTPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国就业与失业数据，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国货币供应量数据，具体指标可参见API文档；历史数据从1995年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国景气指数数据，如商业景气指数、ZEW景气指数、PMI、消费者信息指数，具体指标可参见API文档；历史数据从1985年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国财政收支数据，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataIndustrialPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国工业生产指数数据，具体指标可参见API文档；历史数据从1991年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAINDUSTRIALPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国房地产数据，具体指标可参见API文档；历史数据从2003年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataDomesticTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国国内贸易数据，具体指标可参见API文档；历史数据从1994年开始，按月更新。
        """
        code, result = self.client.getData(vs.GERMANYDATADOMESTICTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def GermanyDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含德国利率数据，具体指标可参见API文档；历史数据从1997年8月开始，按日更新。
        """
        code, result = self.client.getData(vs.GERMANYDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国财政收支数据，具体指标可参见API文档；历史数据从1995年开始，按年更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国GDP数据，具体指标可参见API文档；历史数据从1978年开始，按季更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国对外贸易数据，具体指标可参见API文档；历史数据从1990年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataPPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国生产者价格指数(PPI)数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAPPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataImportPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国进口价格指数数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAIMPORTPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国就业数据，具体指标可参见API文档；历史数据从1983年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国货币供应量数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国景气指数数据，具体指标可参见API文档；历史数据从1985年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataIndustrialPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国工业生产指数数据，具体指标可参见API文档；历史数据从1990年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAINDUSTRIALPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataDomesticTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国国内贸易数据，具体指标可参见API文档；历史数据从1995年开始，按月更新。
        """
        code, result = self.client.getData(vs.FRANCEDATADOMESTICTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FranceDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含法国利率数据，具体指标可参见API文档；历史数据从1980年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.FRANCEDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾GDP数据，具体指标可参见API文档；历史数据从1961年开始，按季更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataExternalDebt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾外债数据，具体指标可参见API文档；历史数据从1999年开始，按季更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAEXTERNALDEBT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾对外贸易数据，具体指标可参见API文档；历史数据从1980年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataImportExportPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾进出口价格指数数据，具体指标可参见API文档；历史数据从1981年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAIMPORTEXPORTPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾就业数据，具体指标可参见API文档；历史数据从1978年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾货币供应量数据，具体指标可参见API文档；历史数据从1961年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataLendingDeposit(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾存贷款数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATALENDINGDEPOSIT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataReserveFund(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾准备金数据，具体指标可参见API文档；历史数据从1998年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATARESERVEFUND%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾景气指数数据，具体指标可参见API文档；历史数据从1982年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataFinance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾财政收支数据，具体指标可参见API文档；历史数据从1961年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAFINANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataIndustrialPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾工业生产指数数据，具体指标可参见API文档；历史数据从1971年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAINDUSTRIALPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾房地产数据，具体指标可参见API文档；历史数据从1991年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataTourism(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾旅游业数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATATOURISM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataCrossStraitTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾两岸贸易数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATACROSSSTRAITTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataBusinessandEconomy(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾商业与经济数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.TAIWANDATABUSINESSANDECONOMY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾利率数据，具体指标可参见API文档；历史数据从2002年5月开始，按日更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TaiwanDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含台湾汇率数据，具体指标可参见API文档；历史数据从1993年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.TAIWANDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门GDP数据，具体指标可参见API文档；历史数据从2000年开始，按季更新。
        """
        code, result = self.client.getData(vs.MACAODATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门价格指数数据，具体指标可参见API文档；历史数据从1998年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门就业数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门货币供应量数据，具体指标可参见API文档；历史数据从1984年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataForeignExchangeReserves(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门外汇储备数据，具体指标可参见API文档；历史数据从1984年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAFOREIGNEXCHANGERESERVES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataTourism(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门旅游业数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATATOURISM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataGamingIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门博彩业数据，具体指标可参见API文档；历史数据从2005年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAGAMINGINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门利率数据，具体指标可参见API文档；历史数据从1988年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MacaoDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含澳门汇率数据，具体指标可参见API文档；历史数据从1984年开始，按月更新。
        """
        code, result = self.client.getData(vs.MACAODATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯GDP数据，具体指标可参见API文档；历史数据从1995年开始，按季更新。
        """
        code, result = self.client.getData(vs.RUSSIADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯对外贸易数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.RUSSIADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从2002年开始，按月更新。
        """
        code, result = self.client.getData(vs.RUSSIADATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯货币供应量数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.RUSSIADATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯景气指数数据，具体指标可参见API文档；历史数据从2009年开始，按月更新。
        """
        code, result = self.client.getData(vs.RUSSIADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯利率数据，具体指标可参见API文档；历史数据从2000年8月开始，按日更新。
        """
        code, result = self.client.getData(vs.RUSSIADATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RussiaDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含俄罗斯汇率数据，具体指标可参见API文档；历史数据从1992年7月开始，按日更新。
        """
        code, result = self.client.getData(vs.RUSSIADATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西GDP数据，具体指标可参见API文档；历史数据从2000年开始，按季更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西对外贸易数据，具体指标可参见API文档；历史数据从1996年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataPriceIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西价格指数数据，具体指标可参见API文档；历史数据从1970年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAPRICEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataEmployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西就业数据，具体指标可参见API文档；历史数据从1997年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西货币供应量数据，具体指标可参见API文档；历史数据从1988年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西景气指数数据，具体指标可参见API文档；历史数据从2007年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataRetailSale(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西零售销售数据，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.BRAZILDATARETAILSALE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西利率数据，具体指标可参见API文档；历史数据从2011年9月开始，按日更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BrazilDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含巴西汇率数据，具体指标可参见API文档；历史数据从1999年4月开始，按日更新。
        """
        code, result = self.client.getData(vs.BRAZILDATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataGDP(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非GDP数据，具体指标可参见API文档；历史数据从1993年开始，按季更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAGDP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataEmploymentUnemployment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非就业与失业数据，具体指标可参见API文档；历史数据从2006年开始，按季更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAEMPLOYMENTUNEMPLOYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataForeignTrade(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非对外贸易数据，具体指标可参见API文档；历史数据从2004年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAFOREIGNTRADE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataCPI(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非消费者价格指数(CPI)数据，具体指标可参见API文档；历史数据从2008年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATACPI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataMoneySupply(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非货币供应量数据，具体指标可参见API文档；历史数据从1965年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAMONEYSUPPLY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataClimateIndex(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非景气指数数据，具体指标可参见API文档；历史数据从1970年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATACLIMATEINDEX%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataIndustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非工业数据，具体指标可参见API文档；历史数据从1993年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataRealEstate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非房地产数据，具体指标可参见API文档；历史数据从1999年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAREALESTATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataRetailSales(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非零售销售数据，具体指标可参见API文档；历史数据从2000年开始，按月更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATARETAILSALES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataInterestRates(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非利率数据，具体指标可参见API文档；历史数据从1980年12月开始，按日更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAINTERESTRATES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SouthAfricaDataExchangeRate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含南非汇率数据，具体指标可参见API文档；历史数据从1970年1月开始，按日更新。
        """
        code, result = self.client.getData(vs.SOUTHAFRICADATAEXCHANGERATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AgricDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含农林牧渔行业价格类数据，即主要农产品价格，主要畜禽产品价格，猪存栏及猪粮比，主要水产品批发价格(威海市)，农产品及农副期货收盘价，消费生产指数，具体指标可参见API文档；历史数据从1947年1月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.AGRICDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AgricDataOutpV(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含农林牧渔行业产值数据，具体指标可参见API文档；历史数据从2000年3月开始，数据按季更新。
        """
        code, result = self.client.getData(vs.AGRICDATAOUTPV%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AgricDataWASDE(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国农业部对全球主要农产品供需预测数据，具体指标可参见API文档；历史数据从1984年6月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.AGRICDATAWASDE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def AgricDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含农林牧渔进出口数据，具体指标可参见API文档；历史数据从1997年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.AGRICDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FoodBvgDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含食品饮料价格类数据，即酒类零售价，乳制品价格，桶装食用油零售价，肉类批发价，调味品零售价，具体指标可参见API文档；历史数据从2004年1月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.FOODBVGDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FoodBvgDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含食品饮料产销及库存数据，具体指标可参见API文档；历史数据从1998年3月开始，数据按季更新。
        """
        code, result = self.client.getData(vs.FOODBVGDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FoodBvgDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含食品饮料进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.FOODBVGDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CommTradeDataTRSCG(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含商品零售及限上收入商品零售社会消费品零售总额数据，具体指标可参见API文档；历史数据从1984年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.COMMTRADEDATATRSCG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CommTradeDataSales50LargeEn(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含50家重点大型零售企业销售数据，具体指标可参见API文档；历史数据从2011年7月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.COMMTRADEDATASALES50LARGEEN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CommTradeDataIndexKeyCircEn(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含商业贸易指数及重点流通企业销售数据，如义乌小商品指数、消费者信心指数、RPI，百货店、超市、专业店销售额等，具体指标可参见API文档；历史数据从1993年12月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.COMMTRADEDATAINDEXKEYCIRCEN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CaterTourDataTRSCG(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含餐饮收入及限上单位餐饮收入社会消费品零售总额数据，具体指标可参见API文档；历史数据从2010年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CATERTOURDATATRSCG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CaterTourDataHotelsOper(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含全国饭店经营性数据，具体指标可参见API文档；历史数据从2011年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CATERTOURDATAHOTELSOPER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CaterTourDataNewHotel(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含全国酒店开业统计数据，具体指标可参见API文档；历史数据从2009年9月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CATERTOURDATANEWHOTEL%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def CaterTourDataInboundTour(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含入境旅游接待收汇数据，具体指标可参见API文档；历史数据从2001年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CATERTOURDATAINBOUNDTOUR%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BioMedicineDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含医药生物行业产销数据,如中成药、化学原料药的产量等，具体指标可参见API文档；历史数据从2001年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.BIOMEDICINEDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BioMedicineDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含医药生物行业进出口数据，如药品、中药材及医疗器械的进出口等，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.BIOMEDICINEDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def PetrochemDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含石油化工行业价格类数据，如石油价格、主要化工产品价格、中纤价格指数等，具体指标可参见API文档；历史数据从1994年1月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.PETROCHEMDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def PetrochemDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含石油化工行业产销及库存数据，具体指标可参见API文档；历史数据从1982年8月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.PETROCHEMDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def PetrochemDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含石油化工行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.PETROCHEMDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ClothTexDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含服装纺织行业价格类数据，如棉花到厂价、中国棉花价格指数、中国纱线价格指数等，具体指标可参见API文档；历史数据从2006年1月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.CLOTHTEXDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ClothTexDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含服装纺织行业产销及库存数据，具体指标可参见API文档；历史数据从1990年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CLOTHTEXDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ClothTexDataCottonWASDE(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含美国农业部对全球棉花供需预测数据，具体指标可参见API文档；历史数据从1984年6月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CLOTHTEXDATACOTTONWASDE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ClothTexDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含服装纺织行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.CLOTHTEXDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def LightManufDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含轻工制造行业价格类数据，如FOEX价格指数，具体指标可参见API文档；历史数据从2012年7月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.LIGHTMANUFDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def LightManufDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含轻工制造行业产销及库存数据，具体指标可参见API文档；历史数据从2001年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.LIGHTMANUFDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def LightManufDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含轻工制造行业进出口数据，具体指标可参见API文档；历史数据从2000年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.LIGHTMANUFDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MiningDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含采掘行业价格类数据，即动力煤、焦煤、焦炭、兰炭价格及煤炭海运运价，具体指标可参见API文档；历史数据从1998年12月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.MININGDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MiningDataOutpSalesTransp(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含采掘行业产销运数据，具体指标可参见API文档；历史数据从2008年4月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.MININGDATAOUTPSALESTRANSP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MiningDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含采掘行业进出口数据，具体指标可参见API文档；历史数据从2000年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.MININGDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FerMetalDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含黑色金属行业价格类数据，如铁矿石价格、螺纹钢价格、线材价格，具体指标可参见API文档；历史数据从2008年12月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.FERMETALDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FerMetalDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含黑色金属行业产销及库存数据，具体指标可参见API文档；历史数据从1998年2月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.FERMETALDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def FerMetalDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含黑色金属行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.FERMETALDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def NonferMetalDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含有色金属行业价格类数据，如铝、铜、铅、锌、锡、镍、金、银等价格类数据，具体指标可参见API文档；历史数据从1968年1月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.NONFERMETALDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def NonferMetalDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含有色金属行业产销及库存数据，具体指标可参见API文档；历史数据从1973年3月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.NONFERMETALDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def NonferMetalDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含有色金属行业进出口数据，具体指标可参见API文档；历史数据从1995年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.NONFERMETALDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def DeliveryEqDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交运设备行业价格类数据，如GAIN市场指数及二手车交易价格等，具体指标可参见API文档；历史数据从2011年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.DELIVERYEQDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def DeliveryEqDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交运设备行业产销数据，如汽车、船舶、飞机等产量，具体指标可参见API文档；历史数据从1958年3月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.DELIVERYEQDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def DeliveryEqDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交运设备行业进出口数据，如汽车、船舶、飞机等进出口，具体指标可参见API文档；历史数据从1998年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.DELIVERYEQDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TrafficTransDataRailway(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交通运输行业中铁路运输数据，如铁路旅客、货物周转量等，具体指标可参见API文档；历史数据从1983年12月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.TRAFFICTRANSDATARAILWAY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TrafficTransDataRoad(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交通运输行业中公路运输数据，如公路旅客、货物周转量等，具体指标可参见API文档；历史数据从1989年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.TRAFFICTRANSDATAROAD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TrafficTransDataWaterway(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交通运输行业中水路运输数据，如波罗的海航运指数，具体指标可参见API文档；历史数据从2007年6月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.TRAFFICTRANSDATAWATERWAY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def TrafficTransDataAir(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含交通运输行业中航空运输数据，如航空运输周转量、航班效率等，具体指标可参见API文档；历史数据从1983年8月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.TRAFFICTRANSDATAAIR%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UtilIndustryDataPower(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含公用事业行业中电力行业数据，如全国发电量、工业用电量等，具体指标可参见API文档；历史数据从1989年3月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.UTILINDUSTRYDATAPOWER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UtilIndustryDataWater(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含公用事业行业中供水行业数据，如行业营收、毛利率等，具体指标可参见API文档；历史数据从2003年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.UTILINDUSTRYDATAWATER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UtilIndustryDataGas(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含公用事业行业中燃气供应数据，如行业营收，毛利率等，具体指标可参见API文档；历史数据从2003年3月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.UTILINDUSTRYDATAGAS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def UtilIndustryDataEnvirProt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含公用事业行业中环保行业数据，如行业固定资产投资及重点城市AQI指数，具体指标可参见API文档；历史数据从2003年3月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.UTILINDUSTRYDATAENVIRPROT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ElecCompDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含电子元件行业价格类数据,如面板价格，电子器件价格指数等，具体指标可参见API文档；历史数据从2007年2月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.ELECCOMPDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ElecCompDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含电子元件行业产销数据及半导体BB值，具体指标可参见API文档；历史数据从1998年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.ELECCOMPDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ElecCompDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含电子元件行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.ELECCOMPDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoEqptDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息设备行业价格类数据，即中国IT市场指数、笔记本市场主流品牌均价、平板电脑市场主流品牌均价，具体指标可参见API文档；历史数据从2007年6月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.INFOEQPTDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoEqptDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息设备行业产销、库存及出货量数据，具体指标可参见API文档；历史数据从1998年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INFOEQPTDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoEqptDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息设备行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INFOEQPTDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HouseholdAplsDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含家用电器行业产销数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.HOUSEHOLDAPLSDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def HouseholdAplsDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含家用电器行业进出口数据，具体指标可参见API文档；历史数据从1998年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.HOUSEHOLDAPLSDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoServDataSoftware(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息服务软件产业数据，即行业收入、行业固定投资、软件覆盖人数、软件总启动次数、软件总使用时长，具体指标可参见API文档；历史数据从2008年8月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.INFOSERVDATASOFTWARE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoServDataComm(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息服务通信产业数据，即通信运营、邮政运营，具体指标可参见API文档；历史数据从1997年12月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INFOSERVDATACOMM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InfoServDataInternet(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含信息服务互联网产业数据，即市场规模、访问次数，具体指标可参见API文档；历史数据从2006年3月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.INFOSERVDATAINTERNET%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RealEstDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含房地产行业价格类数据，如中国一手房价、中国二手房价、全球房价等，具体指标可参见API文档；历史数据从1994年11月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.REALESTDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RealEstDataInvestDvpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含房地产行业投资开发及投资资金来源数据，具体指标可参见API文档；历史数据从1994年2月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.REALESTDATAINVESTDVPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RealEstDataLand(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含房地产行业土地市场数据，如土地成交数据和土地供应数据，具体指标可参见API文档；历史数据从2013年3月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.REALESTDATALAND%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def RealEstDataSales(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含房地产行业销售和库存数据，具体指标可参见API文档；历史数据从1991年2月开始，数据按周更新。
        """
        code, result = self.client.getData(vs.REALESTDATASALES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BldgMaterDataPrice(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含建筑建材行业价格类数据，如水泥价格、玻璃价格等，具体指标可参见API文档；历史数据从2009年12月开始，数据按日更新。
        """
        code, result = self.client.getData(vs.BLDGMATERDATAPRICE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BldgMaterDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含建筑建材行业产销及库存数据，具体指标可参见API文档；历史数据从1990年1月开始，数据按季更新。
        """
        code, result = self.client.getData(vs.BLDGMATERDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MchnrEqptDataSalesOutput(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含机械设备行业产销数据，如仪器仪表产量、专用设备产量、通用设备产量、工程机械产销等，具体指标可参见API文档；历史数据从1990年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.MCHNREQPTDATASALESOUTPUT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def MchnrEqptDataImptExpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含机械设备行业进出口数据，具体指标可参见API文档；历史数据从2010年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.MCHNREQPTDATAIMPTEXPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BankDataAssetsLiabilities(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含银行资产负债数据，如商业银行总资产、总负债等，具体指标可参见API文档；历史数据从2011年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.BANKDATAASSETSLIABILITIES%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def BankDataNonPerformingLoans(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含商业银行业不良贷款数据，如分级别的商业银行不良贷款余额及贷款率，具体指标可参见API文档；历史数据从2003年6月开始，数据按季更新。
        """
        code, result = self.client.getData(vs.BANKDATANONPERFORMINGLOANS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SecuritiesDataOperIndic(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含证券业经营性指标，如证券业总资产、净资本及营收、利润等，具体指标可参见API文档；历史数据从2008年12月开始，数据按半年更新。
        """
        code, result = self.client.getData(vs.SECURITIESDATAOPERINDIC%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InsDataPremPryInsurance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含原保险保费收入数据，如分险种的保费收入，具体指标可参见API文档；历史数据从1999年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INSDATAPREMPRYINSURANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InsDataClaimPayment(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含保险业保险赔付数据，如分险种的保险业务赔款和给付金额，具体指标可参见API文档；历史数据从1999年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INSDATACLAIMPAYMENT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InsDataFundBalance(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含保险资金运用余额数据，如银行存款、股票和债券投资基金等，具体指标可参见API文档；历史数据从1999年1月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INSDATAFUNDBALANCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def InsDataAssets(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            包含保险业总资产和净资产数据，如分险种的保险总资产和净资产，具体指标可参见API文档；历史数据从1999年3月开始，数据按月更新。
        """
        code, result = self.client.getData(vs.INSDATAASSETS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataYili(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含伊利股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAYILI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGuangming(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含光明乳业（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGUANGMING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataChengDeLolo(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含承德露露（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACHENGDELOLO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataQiaqia(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含洽洽食品（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAQIAQIA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataVVGroup(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含维维股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAVVGROUP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJinfengWine(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含金枫酒业（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJINFENGWINE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGuyueLongshan(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含古越龙山（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGUYUELONGSHAN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataShanxiFenjiu(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含山西汾酒（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASHANXIFENJIU%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataZhangyuA(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含张裕A（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAZHANGYUA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMogao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含莫高股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMOGAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataKemenNoodleMFG(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含克明面业（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAKEMENNOODLEMFG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJinziHam(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含金字火腿（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJINZIHAM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLotus(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含莲花味精（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALOTUS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataBeiyinMate(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含贝因美（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABEIYINMATE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataQingdaoHaier(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含青岛海尔（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAQINGDAOHAIER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataTCLGroup(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含TCL集团（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATATCLGROUP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMideaGroup(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含美的集团（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMIDEAGROUP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataWhirlpool(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含惠而浦（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAWHIRLPOOL%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJoyoung(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含九阳股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJOYOUNG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataVatti(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含华帝股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAVATTI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataSupor(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含苏泊尔（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASUPOR%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataKonka(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含深康佳A（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAKONKA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataChanghong(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含四川长虹（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACHANGHONG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLittleSwan(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含小天鹅A（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年10月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALITTLESWAN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMeiling(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含美菱电器（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMEILING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataZTE(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含中兴通讯（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAZTE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataDatangTelecom(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含大唐电信（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATADATANGTELECOM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataBird(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含波导股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABIRD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataDahuaTechnology(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含大华股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATADAHUATECHNOLOGY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataTsinghuaTongfang(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含同方股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATATSINGHUATONGFANG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHedy(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含七喜控股（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年10月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHEDY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHaday(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含海天味业（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHADAY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataYanjingBeer(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含燕京啤酒（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAYANJINGBEER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMaiquer(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含麦趣尔（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年10月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMAIQUER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataCiticGuoanWine(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含中葡股份（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACITICGUOANWINE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataQingqingBarleyWine(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含青青稞酒（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年9月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAQINGQINGBARLEYWINE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHaoxiangni(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含好想你（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHAOXIANGNI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataFulingZhacai(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含涪陵榨菜（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAFULINGZHACAI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHuangshanghuang(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含煌上煌（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHUANGSHANGHUANG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHainanYedao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含海南椰岛（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHAINANYEDAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataShuangtaFood(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含双塔食品（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASHUANGTAFOOD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJiuguiLiquor(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含酒鬼酒（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJIUGUILIQUOR%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataBlackSesame(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含黑芝麻（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABLACKSESAME%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataKingsLuck(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含今世缘（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAKINGSLUCK%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLaobaiganLiquor(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含老白干酒（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALAOBAIGANLIQUOR%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataShuanghuiDvpt(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含双汇发展（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档。历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASHUANGHUIDVPT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataWuliangye(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAWULIANGYE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGree(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGREE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHisenseElectric(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHISENSEELECTRIC%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHisense(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHISENSE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJiajiaFood(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年9月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJIAJIAFOOD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataRobam(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAROBAM%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataASD(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAASD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMacro(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMACRO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataElecpro(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAELECPRO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataSanglejin(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年10月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASANGLEJIN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHoma(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHOMA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLongdaMeat(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALONGDAMEAT%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataByHealth(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABYHEALTH%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHaixin(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHAIXIN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataVanward(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAVANWARD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMeida(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMEIDA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHengshunVinegarindustry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年9月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHENGSHUNVINEGARINDUSTRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataShuijingfang(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASHUIJINGFANG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataChunlan(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACHUNLAN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataYilite(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAYILITE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHuangshi(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHUANGSHI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataYanghe(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAYANGHE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataSanyuan(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASANYUAN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataTuopaiShede(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATATUOPAISHEDE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataKuaijishan(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAKUAIJISHAN%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataTonghua(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATATONGHUA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataKweichowMoutaiGroup(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAKWEICHOWMOUTAIGROUP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataTsingTao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATATSINGTAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGujing(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGUJING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLuzhouLaojiao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALUZHOULAOJIAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataShanghaiMaling(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年8月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASHANGHAIMALING%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataBlackCattleFood(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABLACKCATTLEFOOD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataDelisi(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATADELISI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataStarLakeBioscience(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASTARLAKEBIOSCIENCE%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJonjeeHiTech(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJONJEEHITECH%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataCRSanjiu(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACRSANJIU%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataJiuzhitang(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年11月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAJIUZHITANG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataFuanna(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAFUANNA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLuolai(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALUOLAI%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGuirenniao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGUIRENNIAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataBaoxiniao(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATABAOXINIAO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataLaofengxiang(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATALAOFENGXIANG%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataFiytaA(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAFIYTAA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataGoldleafJewelry(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAGOLDLEAFJEWELRY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataComixGroup(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACOMIXGROUP%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataYaojiPlayingCard(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAYAOJIPLAYINGCARD%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataMGStationery(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAMGSTATIONERY%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataCS(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACS%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataEdifier(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAEDIFIER%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataHikVision(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAHIKVISION%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataSolareast(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATASOLAREAST%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)

    def EcommerceDataChigo(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2014年12月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATACHIGO%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


    def EcommerceDataAucma(self, indicID='', indicName='', beginDate='', endDate='', field=''):
        """
            可包含（公司、业务、产品等维度）电商（淘宝及天猫）数据，具体指标可参见API文档；历史数据从2015年1月开始，数据频度为日度，按月更新。
        """
        code, result = self.client.getData(vs.ECOMMERCEDATAAUCMA%(indicID, indicName, beginDate, endDate, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    
