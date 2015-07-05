#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Created on 2015年7月4日
@author: JimmyLiu
@QQ:52799046
"""
import sys
PY3 = (sys.version_info[0] >= 3)

_MASTER_HEAD = '/api/master/'
_MARKET_HEAD = '/api/market/'
TRADE_DATE = _MASTER_HEAD + 'getTradeCal.csv?exchangeCD=%s&beginDate=%s&endDate=%s&field=%s'
SEC_ID = _MASTER_HEAD + 'getSecID.csv?ticker=%s&partyID=%s&cnSpell=%s&assetClass=%s&field=%s'
EQU_INFO = _MASTER_HEAD + 'getEquInfo.csv?ticker=%s&pagesize=%s&pagenum=%s&field=%s'
REGION = _MASTER_HEAD + 'getSecTypeRegion.csv?field=%s'
REGION_REL = _MASTER_HEAD + 'getSecTypeRegionRel.csv?ticker=%s&typeID=%s&secID=%s&field=%s'
SEC_TYPE = _MASTER_HEAD + 'getSecType.csv?field=%s'
SEC_TYPE_REL = _MASTER_HEAD + 'getSecTypeRel.csv?ticker=%s&typeID=%s&secID=%s&field=%s'

TICK_RT_DEFAULT_COLS = 'shortNM,dataTime,lastPrice,openPrice,highPrice,lowPrice,prevClosePrice'
TICK_RT = _MARKET_HEAD + 'getTickRTSnapshot.csv?securityID=%s&field=%s'
TICK_RT_INDEX = _MARKET_HEAD + 'etTickRTSnapshotIndex.csv?securityID=%s&field=%s'
INDUSTRY_TICK_RT = _MARKET_HEAD + 'getIndustryTickRTSnapshot.csv?securityID=%sfield=%s'
FUTURE_TICK_RT = _MARKET_HEAD + 'getFutureTickRTSnapshot.csv?instrumentID=%s&field=%s'
OPTION_RT = _MARKET_HEAD + 'getOptionTickRTSnapshot.csv?optionId=%s&field=%s'
EQU_RT_RANK = _MARKET_HEAD + 'getEquRTRank.csv?exchangeCD=%s&pagesize=%s&pagenum=%s&desc=%s&field=%s'
SEC_TIPS = _MARKET_HEAD + 'getSecTips.csv?tipsTypeCD=%s&field=%s'
TICK_RT_INTRADAY = _MARKET_HEAD + 'getTickRTIntraDay.csv?securityID=%s&startTime=%s&endTime=%s&field=%s'
BAR_RT = _MARKET_HEAD + 'getBarRTIntraDay.csv?securityID=%s&startTime=%s&endTime=%s&unit=%s&field=%s'