﻿.. tushare documentation master file, created by Jimmy Liu

.. currentmodule:: tushare

.. highlightlang:: python


前言
====

**TuShare是一个免费、开源的python财经数据接口包。**\ 主要实现对股票等金融数据从\ **数据采集**\ 、\ **清洗加工**
到
**数据存储**\ 的过程，能够为金融分析人员提供快速、整洁、和多样的便于分析的数据，为他们在数据获取方面极大地减轻工作量，使他们更加专注于策略和模型的研究与实现上。考虑到Python
pandas包在金融量化分析中体现出的优势，TuShare返回的绝大部分的数据格式都是pandas
DataFrame类型，非常便于用pandas/NumPy/Matplotlib进行数据分析和可视化。当然，如果您习惯了用Excel或者关系型数据库做分析，您也可以通过TuShare的数据存储功能，将数据全部保存到本地后进行分析。应一些用户的请求，从0.2.5版本开始，TuShare同时兼容Python
2.x和Python
3.x，对部分代码进行了重构，并优化了一些算法，确保数据获取的高效和稳定。

TuShare从发布到现在，已经帮助很多用户在数据方面降低了工作压力，同时也得到很多用户的反馈，TuShare将一如既往的用免费和开源的形式分享出来，希望对有需求的人带来一些帮助。如果您觉得TuShare好用并有所收获，请通过\ **微博**\ 、微信或者网站\ **博客**\ 的方式分享出去，让更多的人了解和使用它，使它能在大家的使用过程中逐步得到改进和提升。TuShare还在不断的完善和优化，后期将逐步增加港股、期货、外汇和基金方面的数据，所以，您的支持和肯定才是TuShare坚持下去的动力。

TuShare的数据主要来源于网络，如果在使用过程碰到数据无法获取或发生数据错误的情况，可以通过\ **Email:jimmysoa@sina.cn
QQ:52799046**
联系我，如果有什么好的建议和意见，也请及时联系我，在此谢过。如果在pandas/NumPy技术上有问题，欢迎加入“pandas数据分析”QQ群：297882961（已满），TuShare用户群：14934432，通联数据群：488918622，我会和大家一起帮忙为您解决。

从0.3.8版本开始，TuShare将通联数据开放平台数据接口加入了进来，从数据的丰富性和质量性方面得到了质和量的全面提升，基本上满足了用户对全品类金融数据的需求。

.. figure:: _static/main_pic_min.png
   :alt: 

致谢
----

-  感谢\ `新浪财经 <http://finance.sina.com.cn/>`__\ 、\ `凤凰财经 <http://finance.ifeng.com/>`__\ 、上交所和深交所提供数据
-  感谢深圳大学经济学院研究生\ **邓志浩**\ 的测试和校对
-  感谢上海纽约大学波动研究所\ `赵志强 <http://www.zhihu.com/people/zhao-zhi-qiang-99>`__\ 的审阅
-  感谢在QQ、微博和Email里提出意见和建议的很多个不知道名字的朋友们
-  特别感谢对TuShare进行过捐助的朋友，是你们让我一直保持着更加努力和认真的做事，也让我学会用感恩的心去做好每一件事。

使用对象
--------

-  量化投资分析师（Quant）
-  对金融市场进行大数据分析的企业和个人
-  开发以证券为基础的金融类产品和解决方案的公司
-  正在学习利用python进行数据分析的人

【注：最近有人问到说TuShare不方便看行情，我想说的是，TuShare不是普通炒股者用的软件，而是为那些有兴趣做股票期货数据分析的人提供pandas矩阵数据的工具，至于能不能用来炒股以及效果如何，就看个人的能力了】

使用前提
--------

-  安装Python
-  安装pandas
-  lxml也是必须的，正常情况下安装了Anaconda后无须单独安装，如果没有可执行：pip
   install lxml

建议安装Anaconda（http://www.continuum.io/downloads），一次安装包括了Python环境和全部依赖包，减少问题出现的几率。

下载安装
--------

-  方式1：pip install tushare
-  方式2：访问\ https://pypi.python.org/pypi/tushare/\ 下载安装

版本升级
--------

-  pip install tushare --upgrade

查看当前版本的方法：

::

    import tushare

    print(tushare.__version__)

版本信息
--------

0.4.2 2015/12/27

-  新增电影票房数据
-  修复部分bug

0.4.1

-  新增sina大单数据
-  修改当日分笔bug
-  深市融资融券数据修复

0.3.9

-  新增通联数据期权隐含波动率数据
-  修复指数成份股及权重数据接口

0.3.8

-  完成通联数据SDK v0.2.0开发
-  沪深300成份股和权重接口问题修复
-  其它bug的修复
-  通联数据API文档发布

0.3.5

-  部分代码修正
-  新增通联数据SDK0.1版

0.3.4

-  新增‘龙虎榜’模块

   1. 每日龙虎榜列表
   2. 个股上榜统计
   3. 营业部上榜统计
   4. 龙虎榜机构席位追踪
   5. 龙虎榜机构席位成交明细

-  修改get\_h\_data数据类型为float
-  修改get\_index接口遗漏的open列
-  合并GitHub上提交的bug修复

0.3.1

-  修复get\_h\_data的bug
-  修改get\_stock\_basics数据获取方式
-  0.2.8 2015/04/28

-  新增大盘指数实时行情列表
-  新增大盘指数历史行情数据（全部）
-  新增终止上市公司列表（退市）
-  新增暂停上市公司列表
-  修正融资融券明细无日期的缺陷
-  修正get\_h\_data部分bug

0.2.6 2015/04/22

-  新增沪市融资融券列表
-  新增沪市融资融券明细列表
-  新增深市融资融券列表
-  新增深市融资融券明细列表
-  修正复权数据数据源出现null造成异常问题（对大约300个股票有影响）

0.2.5 2015/04/16

-  完成python2.x和python3.x兼容性支持
-  部分算法优化和代码重构
-  新增中证500成份股
-  新增当日分笔交易明细
-  修正分配预案（高送转）bug

0.2.3 2015/04/11

-  新增“新浪股吧”消息和热度
-  新增新股上市数据
-  修正“基本面”模块中数据重复的问题
-  修正历史数据缺少一列column（数据来源问题）的bug

0.2.0 2015/03/17

-  新增历史复权数据接口
-  新增即时滚动新闻、信息地雷数据
-  新增沪深300指数成股份及动态权重、
-  新增上证50指数成份股
-  修改历史行情数据类型为float

0.1.9 2015/02/06

-  增加分类数据
-  增加数据存储示例

0.1.6 2015/01/27

-  增加了重点指数的历史和实时行情
-  更新docs

0.1.5 2015/01/26

-  增加基本面数据接口
-  发布一版使用手册，开通\ `TuShare
   docs <http://tushare.waditu.com>`__\ 网站

0.1.3 2015/01/13

-  增加实时交易数据的获取
-  Done for crawling Realtime Quotes data

0.1.1 2015/01/11

-  增加tick数据的获取

0.1.0 2014/12/01

-  创建第一个版本
-  实现个股历史数据的获取

友情链接
--------

-  `大数据导航 <http://hao.199it.com/jrsj.html>`__
-  `RiceQuant <https://www.ricequant.com/>`__
-  `JoinQuant <https://www.joinquant.com/>`__









.. toctree::
    :maxdepth: 2
    
    index
    trading
    reference
    classifying
    fundamental
    macro
    newsevent
    billboard
    shibor
    storing
    datayes
    boxoffice
    donate
    
