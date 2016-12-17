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

class Subject():
    
    def __init__(self, client=None):
        if client is None:
            self.client = Client(up.get_token())
        else:
            self.client = client
            
            
    def SocialDataXQ(self, beginDate='', endDate='', ticker='', field=''):
        """
            包含雪球社交统计数据，输入一个或多个证券交易代码、统计起止日期，获取该证券一段时间内每天的雪球帖子数量、帖子占比(%)。(注：数据自2014/1/1始，按日更新。)
        """
        code, result = self.client.getData(vs.SOCIALDATAXQ%(beginDate, endDate, ticker, field))
        return _ret_data(code, result)

    def SocialDataXQByTicker(self, ticker='', field=''):
        """
            包含按单只证券代码获取的雪球社交数据，输入一个证券交易代码，获取该证券每天的雪球帖子数量、及帖子占比(%)。(注：数据自2014/1/1始，按日更新。)
        """
        code, result = self.client.getData(vs.SOCIALDATAXQBYTICKER%(ticker, field))
        return _ret_data(code, result)

    def SocialDataXQByDate(self, statisticsDate='', field=''):
        """
            包含按单个统计日期获取的雪球社交数据，输入一个统计日期，获取当天雪球帖子涉及的所有证券、各证券雪球帖子数量、帖子占比(%)。(注：数据自2014/1/1始，按日更新。)
        """
        code, result = self.client.getData(vs.SOCIALDATAXQBYDATE%(statisticsDate, field))
        return _ret_data(code, result)

    def NewsInfo(self, newsID='', field=''):
        """
            包含新闻基本信息。输入新闻ID，获取新闻基本信息，如：新闻ID、标题、摘要、初始来源、作者、发布来源、发布时间、入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、每天新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSINFO%(newsID, field))
        return _ret_data(code, result)

    def NewsInfoByTime(self,  newsPublishDate='', beginTime='', endTime='', field=''):
        """
            获取某天某一段时间内的新闻基本信息。输入新闻发布的日期、起止时间，获取该时间段内的新闻相关信息，如：新闻ID、标题、摘要、初始来源、作者、发布来源、发布时间、入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSINFOBYTIME%(newsPublishDate, beginTime, endTime, field))
        return _ret_data(code, result)

    def NewsContent(self, newsID='', field=''):
        """
            包含新闻全文等信息。输入新闻ID，获取新闻全文相关字段，如：新闻ID、标题、摘要、正文、来源链接、初始来源、作者、发布来源、发布时间、入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSCONTENT%(newsID, field))
        return _ret_data(code, result)

    def NewsContentByTime(self, newsPublishDate='', beginTime='', endTime='', field=''):
        """
            获取某天某一段时间内的新闻全文等信息。输入新闻发布的日期、起止时间，获取该时间段内的新闻全文等信息，如：新闻ID、标题、摘要、正文、来源链接、初始来源、作者、发布来源、发布时间、入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSCONTENTBYTIME%(newsPublishDate, beginTime, endTime, field))
        return _ret_data(code, result)

    def CompanyByNews(self, newsID='', field=''):
        """
            包含新闻关联的公司数据，同时可获取针对不同公司的新闻情感数据。输入新闻ID，获取相关的公司信息，如：公司代码、公司全称，同时返回新闻标题、发布时间、入库时间信息。其中，公司代码可继续通过证券编码及基本上市信息(getSecID)查找公司相关的证券。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.COMPANYBYNEWS%(newsID, field))
        return _ret_data(code, result)

    def NewsByCompany(self, partyID='', beginDate='', endDate='', field=''):
        """
            包含公司关联的新闻数据，同时可获取针对不同公司的新闻情感数据。输入公司代码、查询的新闻发布起止时间，获取相关的新闻信息，如：新闻ID、新闻标题、发布来源、发布时间、新闻入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSBYCOMPANY%(partyID, beginDate, endDate, field))
        return _ret_data(code, result)

    def TickersByNews(self, newsID='', field=''):
        """
            包含新闻相关的证券数据，同时可获取针对不同证券的新闻情感数据。输入新闻ID，获取相关的证券信息，如：证券代码、证券简称、证券交易场所，同时返回新闻标题、发布来源、发布时间、入库时间等新闻相关信息。每天更新。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.TICKERSBYNEWS%(newsID, field))
        return _ret_data(code, result)

    def NewsByTickers(self, secID='', secShortName='', ticker='', beginDate='', endDate='', exchangeCD='', field=''):
        """
            包含证券相关的新闻数据，同时可获取针对不同证券的新闻情感数据。输入证券代码或简称、查询的新闻发布起止时间，同时可输入证券交易所代码，获取相关新闻数据，如：新闻ID、新闻标题、发布来源、发布时间、入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSBYTICKERS%(secID, secShortName, ticker, beginDate, endDate, exchangeCD, field))
        return _ret_data(code, result)

    def ThemesContent(self, isMain='', themeID='', themeName='', themeSource='', field=''):
        """
            包含所有主题基本信息。输入主题代码或名称、主题来源，可以获取主题相关信息，包括主题ID、主题名称、主题描述、主题来源、当天是否活跃、主题插入时间、主题更新时间等。(注：1、主题基期自2011/4/16始；2、数据按日更新主题活跃状态。)
        """
        code, result = self.client.getData(vs.THEMESCONTENT%(isMain, themeID, themeName, themeSource, field))
        return _ret_data(code, result)

    def TickersByThemes(self, themeID='', themeName='', beginDate='', endDate='', isNew='', field=''):
        """
            包含主题关联的证券数据。输入主题代码或名称，可以获取主题关联的证券等信息，包括证券代码、证券简称、证券交易场所，同时返回三个维度的关联分数、关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间，同时可输入查询起止时间，以获取主题在该时间段内关联的证券信息。(注：1、主题与证券的关联自2013/12/28始、2014年12月起关联数据完整；2、数据按日更新、同时刷新关联状态。)
        """
        code, result = self.client.getData(vs.TICKERSBYTHEMES%(themeID, themeName, beginDate, endDate, isNew, field))
        return _ret_data(code, result)

    def ThemesTickersInsert(self, themeID='', themeName='', beginDate='', endDate='', field=''):
        """
            获取一段时间内主题新增的关联证券数据，输入主题代码或名称、查询起止时间，可以获取该时间段内主题新增的关联证券信息，包括证券代码、证券简称、证券交易场所，同时返回三个维度的关联分数、关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间。(注：1、主题与证券的关联自2013/12/28始、2014年12月起关联数据完整；2、数据按日更新。)
        """
        code, result = self.client.getData(vs.THEMESTICKERSINSERT%(themeID, themeName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThemesTickersDelete(self, themeID='', themeName='', beginDate='', endDate='', field=''):
        """
            获取一段时间内主题删除的关联证券数据，输入主题代码或名称、查询起止时间，可以获取该时间段内主题删除的关联证券信息，包括证券代码、证券简称、证券交易场所，同时返回关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间。(注：1、主题与证券的关联自2013/12/28始、2014年12月起关联数据完整；2、数据按日更新。)
        """
        code, result = self.client.getData(vs.THEMESTICKERSDELETE%(themeID, themeName, beginDate, endDate, field))
        return _ret_data(code, result)

    def ThemesByTickers(self, secID='', secShortName='', ticker='', beginDate='', endDate='', exchangeCD='', field=''):
        """
            包含证券关联的主题数据。输入证券交易所代码、证券交易代码或简称，可以获取关联的主题等信息，包括证券代码、证券简称、证券交易场所，同时返回三个维度的关联分数、关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间，同时可输入查询起止时间，以获取证券在该时间段内关联到的主题信息。(注：1、主题与证券的关联自2013/12/28始、2014年12月起关联数据完整；2、数据按日更新。)
        """
        code, result = self.client.getData(vs.THEMESBYTICKERS%(secID, secShortName, ticker, beginDate, endDate, exchangeCD, field))
        return _ret_data(code, result)

    def ThemesPeriod(self, isLatest='', themeID='', themeName='', field=''):
        """
            包含主题活跃周期数据。输入主题代码或名称，获取主题的活跃时间等信息，同时可输入是否最新活跃期，获取主题最新的活跃周期。(注：1、主题活跃周期数据自2013/1/1始；2、新闻量在某段时间内达到活跃阈值的主题即为活跃主题；3、数据按日更新。)
        """
        code, result = self.client.getData(vs.THEMESPERIOD%(isLatest, themeID, themeName, field))
        return _ret_data(code, result)

    def ActiveThemes(self, date='', field=''):
        """
            获取某天活跃的主题数据。输入一个日期，获取在该日期活跃的主题。(注：1、主题活跃周期数据自2013/1/1始；2、新闻量在某段时间内达到活跃阈值的主题即为活跃主题；3、数据按日更新。)
        """
        code, result = self.client.getData(vs.ACTIVETHEMES%(date, field))
        return _ret_data(code, result)

    def ThemesSimilarity(self, themeID='', themeName='', field=''):
        """
            获取与某主题相似的其他主题数据。输入主题代码或名称，可以获取相似的主题信息，包括相似主题代码、相似主题名称、主题文本的相似度、主题关联证券的相似度。数据按日更新。
        """
        code, result = self.client.getData(vs.THEMESSIMILARITY%(themeID, themeName, field))
        return _ret_data(code, result)

    def ThemesHeat(self, themeID='', themeName='', beginDate='', endDate='', field=''):
        """
            包含主题的热度数据。输入主题代码或名称、同时可输入起止日期，获取一段时间内主题每天的新闻数量、主题热度(即主题每天新闻数量占当日所有主题新闻总量的百分比(%))。(注：数据自2014/1/1始，每天更新)
        """
        code, result = self.client.getData(vs.THEMESHEAT%(themeID, themeName, beginDate, endDate, field))
        return _ret_data(code, result)

    def SectorThemesByTickers(self, secID='', secShortName='', ticker='', beginDate='', endDate='', exchangeCD='', field=''):
        """
            包含证券关联的主题数据，主题源自申万行业。输入证券交易所代码、证券交易代码或简称，可以获取关联的主题等信息，包括证券代码、证券简称、证券交易场所，同时返回三个维度的关联分数、关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间，同时可输入查询起止时间，以获取证券在该时间段内关联到的主题信息。(注：1、源自行业的主题与证券的关联自2014/12/26始；2、数据按日更新、同时刷新关联状态。)
        """
        code, result = self.client.getData(vs.SECTORTHEMESBYTICKERS%(secID, secShortName, ticker, beginDate, endDate, exchangeCD, field))
        return _ret_data(code, result)

    def WebThemesByTickers(self, secID='', secShortName='', ticker='', beginDate='', endDate='', exchangeCD='', field=''):
        """
            包含证券关联的主题数据，主题源自网络。输入证券交易所代码、证券交易代码或简称，可以获取关联的主题等信息，包括证券代码、证券简称、证券交易场所，同时返回三个维度的关联分数、关联开始时间、关联结束时间、关联具体描述、数据入库及更新时间，同时可输入查询起止时间，以获取证券在该时间段内关联到的主题信息。(注：1、源自网络的主题与证券的关联自2013/12/28始、2014年12月起关联数据完整；2、数据按日更新。)
        """
        code, result = self.client.getData(vs.WEBTHEMESBYTICKERS%(secID, secShortName, ticker, beginDate, endDate, exchangeCD, field))
        return _ret_data(code, result)

    def NewsHeatIndex(self, beginDate='', endDate='', exchangeCD='', secID='', secShortName='', ticker='', field=''):
        """
            包含证券相关的新闻热度指数数据，输入一个或多个证券交易代码、起止日期，获取该证券一段时间内的新闻热度指数(即证券当天关联新闻数量占当天新闻总量的百分比(%))。每天更新。（注：1、2014/1/1起新闻来源众多、指数统计有效，2013年及之前的网站来源不全、数据波动大，数据自2004/10/28始；2、新闻量的统计口径为经算法处理后证券关联到的所有常规新闻；3、数据按日更新。)
        """
        code, result = self.client.getData(vs.NEWSHEATINDEX%(beginDate, endDate, exchangeCD, secID, secShortName, ticker, field))
        return _ret_data(code, result)

    def NewsSentimentIndex(self, beginDate='', endDate='', exchangeCD='', secID='', secShortName='', ticker='', field=''):
        """
            包含证券相关的新闻情感指数数据，输入一个或多个证券交易代码、起止日期，获取该证券一段时间内的新闻情感指数(即当天证券关联新闻的情感均值)。（注：1、2014/1/1起新闻来源众多、指数统计有效，2013年及之前的网站来源不全、数据波动大，数据自2004/10/28始；2、新闻量的统计口径为经算法处理后证券关联到的所有常规新闻；3、数据按日更新。)
        """
        code, result = self.client.getData(vs.NEWSSENTIMENTINDEX%(beginDate, endDate, exchangeCD, secID, secShortName, ticker, field))
        return _ret_data(code, result)

    def ReportByTicker(self, ticker='', beginDate='', endDate='', field=''):
        """
            根据证券代码获取相应公告分类结果，输入一个或多个证券交易代码，可以获取所查询证券相关的公告信息，包括公告ID、公告名称、证券交易场所、证券交易所对公告的原始分类、公告分类结果、公告分类入库时间、更新时间。(注：公告分类数据自2009/1/5始，按日更新)
        """
        code, result = self.client.getData(vs.REPORTBYTICKER%(ticker, beginDate, endDate, field))
        return _ret_data(code, result)

    def ReportByCategory(self, beginDate='', Category='', endDate='', field=''):
        """
            根据公告分类获取相应公告信息，输入一个或多个公告分类，可以获取所查询证券相关的公告信息，包括公告ID、公告名称、证券交易场所、证券交易所对公告的原始分类、公告发布时间、公告所属分类、公告分类入库时间、更新时间。(注：公告分类数据自2009/1/5始，按日更新)
        """
        code, result = self.client.getData(vs.REPORTBYCATEGORY%(beginDate, Category, endDate, field))
        return _ret_data(code, result)

    def ReportContent(self, ticker='', beginDate='', endDate='', field=''):
        """
            根据证券代码获取公告内容，输入一个或多个证券交易代码，可以获取所查询证券相关的公告信息，包括公告ID、公告名称、证券交易场所、证券交易所对公告的原始分类、公告发布时间、公告具体内容、公告链接、公告入库时间。(注：公告数据自2000/1/8始，按日更新)
        """
        code, result = self.client.getData(vs.REPORTCONTENT%(ticker, beginDate, endDate, field))
        return _ret_data(code, result)

    def ActiveThemesInsert(self, beginDate='', endDate='', isLatest='', themeSource='', field=''):
        """
            获取一段时间内新增(开始)的活跃主题数据，输入的时间参数在主题活跃周期的起始时间列进行查询。输入查询起止时间、是否最新活跃期、主题来源，可以获取该时间段内开始活跃的主题信息，包括主题ID、主题名称、主题开始时间、主题结束时间、是否最新活跃期、数据入库及更新时间。(注：1、主题活跃周期数据自2013/1/1始；2、数据按日更新。)
        """
        code, result = self.client.getData(vs.ACTIVETHEMESINSERT%(beginDate, endDate, isLatest, themeSource, field))
        return _ret_data(code, result)

    def ActiveThemesDelete(self, beginDate='', endDate='', isLatest='', themeSource='', field=''):
        """
            获取一段时间内删除(退出)的活跃主题数据，输入的时间参数在主题活跃周期的结束时间列进行查询。输入查询起止时间、是否最新活跃期、主题来源，可以获取该时间段内停止活跃的主题信息，包括主题ID、主题名称、主题开始时间、主题结束时间、是否最新活跃期、数据入库及更新时间。(注：1、主题活跃周期数据自2013/1/1始；2、数据按日更新。3、查询当天无活跃主题被删除、需等第二天9:00之后获取前一天停止活跃的主题数据。)
        """
        code, result = self.client.getData(vs.ACTIVETHEMESDELETE%(beginDate, endDate, isLatest, themeSource, field))
        return _ret_data(code, result)

    def ThemesCluster(self, isMain='', themeID='', themeName='', field=''):
        """
            获取当天活跃主题聚类对应关系数据。输入聚类后的主要主题代码或名称，可以获取同一类别的主题相关信息，包括主题ID、主题名称、主题插入时间、主题更新时间等。(注：1、可先在主题基本信息(getThemesContent)这个API中获取当天聚类后的主题；2、可输入isMain=0，在返回的数据中剔除主题自身的对应；3、数据每天刷新，只能获取当天数据。)
        """
        code, result = self.client.getData(vs.THEMESCLUSTER%(isMain, themeID, themeName, field))
        return _ret_data(code, result)

    def ThemesByNews(self, insertDate='', newsID='', beginTime='', endTime='', field=''):
        """
            获取新闻关联的主题数据。输入新闻ID或新闻与主题的关联数据入库起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWS%(insertDate, newsID, beginTime, endTime, field))
        return _ret_data(code, result)

    def ThemesByNewsCompanyRel(self, insertDate='', newsID='', beginTime='', endTime='', field=''):
        """
            获取新闻关联的主题数据，只包含与公司相关的新闻。输入新闻ID或新闻与主题的关联数据入库起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSCOMPANYREL%(insertDate, newsID, beginTime, endTime, field))
        return _ret_data(code, result)

    def ThemesInsertDB(self, beginDate='', endDate='', themeSource='', field=''):
        """
            获取一段时间内新入库的主题数据。输入查询起止时间，可以获取该时间段内新入库的主题信息，包括主题ID、主题名称、主题描述、主题来源、当天是否活跃、主题插入时间、主题更新时间等。(注：1、主题基期自2011/4/16始；2、数据按日更新主题活跃状态。)
        """
        code, result = self.client.getData(vs.THEMESINSERTDB%(beginDate, endDate, themeSource, field))
        return _ret_data(code, result)

    def ThemesByNewsLF(self, insertDate='', newsID='', beginTime='', endTime='', field=''):
        """
            获取新闻关联的主题数据，该API以获取新闻关联的主题(getThemesByNews)为基础、进行过滤优化。输入新闻ID或新闻与主题的关联数据入库起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSLF%(insertDate, newsID, beginTime, endTime, field))
        return _ret_data(code, result)

    def ThemesByNewsMF(self, insertDate='', newsID='', beginTime='', endTime='', field=''):
        """
            获取新闻关联的主题数据，该API以获取新闻关联的主题(优化后)(getThemesByNewsLF)为基础、再次进行过滤优化，是所有获取新闻关联的主题API中最严格的优化结果、数据量也最少。输入新闻ID或新闻与主题的关联数据入库起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSMF%(insertDate, newsID, beginTime, endTime, field))
        return _ret_data(code, result)

    def NewsInfoByInsertTime(self, newsInsertDate='', beginTime='', endTime='', field=''):
        """
            获取某天某一段时间内入库的新闻基本信息。输入新闻入库的日期、起止时间，获取该时间段内新入库的新闻相关信息，如：新闻ID、标题、摘要、初始来源、作者、发布来源、发布时间、新闻入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSINFOBYINSERTTIME%(newsInsertDate, beginTime, endTime, field))
        return _ret_data(code, result)

    def NewsContentByInsertTime(self, newsInsertDate='', beginTime='', endTime='', field=''):
        """
            获取某天某一段时间内入库的新闻全文等信息。输入新闻入库的日期、起止时间，获取该时间段内新入库的新闻全文等信息，如：新闻ID、标题、摘要、正文、来源链接、初始来源、作者、发布来源、发布时间、新闻入库时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新。)
        """
        code, result = self.client.getData(vs.NEWSCONTENTBYINSERTTIME%(newsInsertDate, beginTime, endTime, field))
        return _ret_data(code, result)

    def SocialDataGuba(self, beginDate='', endDate='', ticker='', field=''):
        """
            包含证券在股吧社交中的热度统计数据，输入一个或多个证券交易代码、统计起止日期，该证券在一段时间内每天相关的股吧帖子数量、帖子占比(%)。(注：数据自2014/1/1始，按日更新。)
        """
        code, result = self.client.getData(vs.SOCIALDATAGUBA%(beginDate, endDate, ticker, field))
        return _ret_data(code, result)

    def SocialThemeDataGuba(self, beginDate='', endDate='', themeID='', field=''):
        """
            包含主题在股吧社交中的热度统计数据，输入一个或多个主题代码、统计起止日期，获取该主题在一段时间内每天相关的股吧帖子数量、帖子占比(%)。(注：数据自2014/1/1始，按日更新。)
        """
        code, result = self.client.getData(vs.SOCIALTHEMEDATAGUBA%(beginDate, endDate, themeID, field))
        return _ret_data(code, result)

    def ThemesByNewsTime(self, publishBeginTime='', publishEndTime='', field=''):
        """
            根据发布时间获取新闻关联的主题数据。输入新闻发布的起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSTIME%(publishBeginTime, publishEndTime, field))
        return _ret_data(code, result)

    def ThemesByNewsTimeCompanyRel(self, publishBeginTime='', publishEndTime='', field=''):
        """
            根据发布时间获取新闻关联的主题数据，只包含与公司相关的新闻。输入新闻发布的起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSTIMECOMPANYREL%(publishBeginTime, publishEndTime, field))
        return _ret_data(code, result)

    def ThemesByNewsTimeLF(self, publishBeginTime='', publishEndTime='', field=''):
        """
            根据发布时间获取新闻关联的主题数据，该API以获取新闻关联的主题(getThemesByNewsTime)为基础、进行过滤优化。输入新闻发布的起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSTIMELF%(publishBeginTime, publishEndTime, field))
        return _ret_data(code, result)

    def ThemesByNewsTimeMF(self, publishBeginTime='', publishEndTime='', field=''):
        """
            根据发布时间获取新闻关联的主题数据，该API以获取新闻关联的主题(优化后)(getThemesByNewsTimeLF)为基础、再次进行过滤优化，是所有获取新闻关联的主题API中最严格的优化结果、数据量也最少。输入新闻发布的起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/04/07。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSTIMEMF%(publishBeginTime, publishEndTime, field))
        return _ret_data(code, result)

    def ReportContentByID(self, reportID='', field=''):
        """
            根据公告ID获取公告原始内容数据，输入公告ID，获取公告原文等信息，包括公告ID、公告名称、证券交易场所、证券交易所对公告的原始分类、公告发布时间、公告具体内容、公告链接、公告入库时间。(注：公告数据自2000/1/8始，按日更新)
        """
        code, result = self.client.getData(vs.REPORTCONTENTBYID%(reportID, field))
        return _ret_data(code, result)

    def ThemesByNews2(self, insertBeginTime='', insertEndTime='', newsID='', field=''):
        """
            获取新闻关联的主题数据，原API(获取新闻关联的主题数据-getThemesByNews)的升级版。输入新闻ID或新闻与主题的关联数据入库起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/06/17)
        """
        code, result = self.client.getData(vs.THEMESBYNEWS2%(insertBeginTime, insertEndTime, newsID, field))
        return _ret_data(code, result)

    def ThemesByNewsTime2(self, publishBeginTime='', publishEndTime='', field=''):
        """
            根据发布时间获取新闻关联的主题数据，原API(根据发布时间获取新闻关联的主题数据-getThemesByNewsTime)的升级版。输入新闻发布的起止时间，可以获取相关的主题信息，如：主题ID、主题名称，同时返回新闻标题、新闻发布时间、关联数据入库时间、更新时间等。(注：1、自2014/1/1起新闻来源众多、新闻量日均4万左右，2013年及之前的网站来源少、新闻数据量少；2、数据实时更新；3、关联数据入库起始时间为2015/06/17。)
        """
        code, result = self.client.getData(vs.THEMESBYNEWSTIME2%(publishBeginTime, publishEndTime, field))
        return _ret_data(code, result)


def _ret_data(code, result):
    if code==200:
        result = result.decode('utf-8') if vs.PY3 else result
        df = pd.read_csv(StringIO(result))
        return df
    else:
        print(result)
        return None    
    