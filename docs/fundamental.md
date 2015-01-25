.. highlightlang:: python

基本面数据获取
=========
*基本面类数据*提供所有股票的基本面情况，包括股本情况、业绩预告和业绩预告等。主要包括以下类别：

- 沪深股票列表
- 业绩预告
- 业绩报告（主表）
- 盈利能力数据
- 营运能力数据
- 成长能力数据
- 偿债能力数据
- 现金流量数据

本模块数据全部来自sina财经，由于财务数据项目比较多，所以拆分成了几个表，使用时可以通过股票代码合并在一起，也可以独立使用。数据在获取时，需要一页一页的抓取，所以需要一点等待时间，最后会合并成一个大表。

沪深股票列表数据
------------
获取沪深上市公司基本情况。属性包括：

	   code,代码
	   name,名称
	   industry,所属行业
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

由于目前暂时没有找到能便捷获取股本等信息的web接口，现在是以直接读取文件（data/all.csv）的方式实现，所以需要定期更新。或者按以上columns自行从行情软件导出数据。

    In[1]:import tushare.stock.fundamental as fd

	In[2]:fd.get_stock_basics()

结果显示：

    