#!/usr/bin/env python
# -*- coding:utf-8 -*- 

'''
Created on 2016年9月25日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
'''
import six
import pandas as pd
import requests
import time
from threading import Thread
from tushare.trader import vars as vs
from tushare.trader import utils
from tushare.util import upass as up


class TraderAPI(object):
    """
    股票实盘交易接口
    """
    def __init__(self, broker = ''):
        if broker == '':
            return None
        self.broker = broker
        self.trade_prefix = vs.CSC_PREFIX % (vs.P_TYPE['https'], 
                                             vs.DOMAINS['csc'],
                                             vs.PAGES['csclogin'])
        self.heart_active = True
        self.s = requests.session()
        if six.PY2:
            self.heart_thread = Thread(target = self.send_heartbeat)
            self.heart_thread.setDaemon(True)
        else:
            self.heart_thread = Thread(target = self.send_heartbeat, 
                                       daemon=True)
            
            
    def login(self):
        self.s.headers.update(vs.AGENT)
        self.s.get(vs.CSC_PREFIX % (vs.P_TYPE['https'], vs.DOMAINS['csc'],
                                             vs.PAGES['csclogin']))
        if self._login('') is False:
            print('请确认账号或密码是否正确 ，或券商服务器是否处于维护中。 ')
        self.keepalive()
        
        
    def _login(self, v_code):
        brokerinfo = up.get_broker(self.broker)
        user = brokerinfo['user'][0]
        login_params = dict(
            inputid = user,                                 
            j_username = user,
            j_inputid = user,
            j_password = brokerinfo['passwd'][0]
        )
        logined = self.s.post(vs.CSC_LOGIN_ACTION % (vs.P_TYPE['https'], 
                                                     vs.DOMAINS['csc']), 
                              params = login_params)
        if logined.text.find(u'消息中心') != -1:
            return True
        return False
    
    
    def keepalive(self):
        if self.heart_thread.is_alive():
            self.heart_active = True
        else:
            self.heart_thread.start()


    def send_heartbeat(self):
        while True:
            if self.heart_active:
                try:
                    response = self.heartbeat()
                    self.check_account_live(response)
                except:
                    self._login('')
                time.sleep(10)
            else:
                time.sleep(1)


    def heartbeat(self):
        return self.baseinfo


    def exit(self):
        self.heart_active = False

    
    def buy(self, stkcode, price=0, count=0, amount=0):
        """
    买入证券
        params
        ---------
        stkcode:股票代码，string
        pricce:委托价格，int
        count:买入数量
        amount:买入金额
        """
        jsonobj = utils.get_jdata(self._trading(stkcode, price, 
                                                count, amount, 'B', 'buy'))
        res = True if jsonobj['result'] == 'true' else False
        return res
        
    
    def sell(self, stkcode, price=0, count=0, amount=0):
        """
    卖出证券
        params
        ---------
        stkcode:股票代码，string
        pricce:委托价格，int
        count:卖出数量
        amount:卖出金额
        """
        jsonobj = utils.get_jdata(self._trading(stkcode, price, count, 
                                                amount, 'S', 'sell'))
        res = True if jsonobj['result'] == 'true' else False
        return res
    
    
    def _trading(self, stkcode, price, count, amount, tradeflag, tradetype):
        txtdata = self.s.get(vs.TRADE_CHECK_URL % (vs.P_TYPE['https'], 
                                                   vs.DOMAINS['csc'], 
                                                   vs.PAGES['tradecheck'],
                                                   tradeflag, stkcode, 
                                                   tradetype, utils.nowtime_str()))
        jsonobj = utils.get_jdata(txtdata)
        list = jsonobj['returnList'][0]
        secuid = list['buysSecuid']
        fundavl = list['fundavl']
        stkname = list['stkname']
        if secuid is not None:
            if tradeflag == 'B':
                buytype = vs.BUY
                count = count if count else amount // price // 100 * 100 
            else:
                buytype = vs.SELL
                count = count if count else amount // price
                
            tradeparams = dict(
            stkname = stkname,
            stkcode = stkcode,
            secuid = secuid,
            buytype = buytype,
            bsflag = tradeflag,
            maxstkqty = '',
            buycount = count,
            buyprice = price,
            _ = utils.nowtime_str()
            )
            tradeResult = self.s.post(vs.TRADE_URL % (vs.P_TYPE['https'], 
                                                      vs.DOMAINS['csc'], 
                                                      vs.PAGES['trade']), 
                        params = tradeparams)
            return tradeResult
        return None
        

    def position(self):
        """
    获取持仓列表
        return:DataFrame
        ----------------------
        stkcode:证券代码
        stkname:证券名称
        stkqty :证券数量
        stkavl :可用数量
        lastprice:最新价格
        costprice:成本价
        income :参考盈亏（元）
        """
        return self._get_position()
    
    
    def _get_position(self):
        self.s.headers.update(vs.AGENT)
        txtdata = self.s.get(vs.BASE_URL % (vs.P_TYPE['https'], 
                                            vs.DOMAINS['csc'], 
                                            vs.PAGES['position']))
        jsonobj = utils.get_jdata(txtdata)
        df = pd.DataFrame(jsonobj['data'], columns=vs.POSITION_COLS)
        return df
    
    
    def entrust_list(self):
        txtdata = self.s.get(vs.ENTRUST_LIST_URL % (vs.P_TYPE['https'], 
                                                    vs.DOMAINS['csc'], 
                                                    vs.PAGES['entrustlist'],
                                            utils.nowtime_str()))
        jsonobj = utils.get_jdata(txtdata)
        df = pd.DataFrame(jsonobj['data'], columns=vs.ENTRUST_LIST_COLS)
        return df
    
    
    def deal_list(self, begin=None, end=None):
        """
    获取成交列表
        params
        -----------
        begin:开始日期  YYYYMMDD
        end:结束日期  YYYYMMDD
        
        return: DataFrame
        -----------
        trddate:交易日期
        matchtime:交易时间
        stkcode:证券代码
        stkname:证券名称
        bsflagState:买卖标志
        orderprice:委托价格
        matchprice:成交价格
        orderqty:委托数量
        matchqty:成交数量
        matchamt:成交金额
        """
        daterange = ''
        if (begin is None) & (end is None):
            selecttype = 'intraDay'
        else:
            daterange = vs.DEAL_DATE_RANGE % (begin, end)
            selecttype = 'all'
        txtdata = self.s.get(vs.DEAL_LIST_URL % (vs.P_TYPE['https'], 
                                                 vs.DOMAINS['csc'], 
                                                 vs.PAGES['deallist'],
                                                 selecttype, daterange, 
                                                 utils.nowtime_str()))
        jsonobj = utils.get_jdata(txtdata)
        df = pd.DataFrame(jsonobj['data'], columns=vs.DEAL_LIST_COLS)
        return df
    
    
    def cancel(self, ordersno='', orderdate=''):
        """
                 撤单
        params
        -----------
        ordersno:委托单号，多个以逗号分隔，e.g. 1866,1867
        orderdata:委托日期 YYYYMMDD，多个以逗号分隔，对应委托单好
        return
        ------------
        string
        """
        if (ordersno != '') & (orderdate != ''):
            params = dict(
                  ordersno = ordersno,
                  orderdate = orderdate,
                  _ = utils.nowtime_str()             
                               
            )
            result = self.s.post(vs.CANCEL_URL % (vs.P_TYPE['https'], vs.DOMAINS['csc'], vs.PAGES['cancel']), 
                            params = params)   
            return result.text
        return None
    
    
    def baseinfo(self):
        """
    获取帐户基本信息
        return: Series
        -------------
        fundid:帐户ID
        gpsz: 股票市值
        fundvalue:基金市值
        jihelicai:集合理财
        fundbal:帐户余额
        marketvalue:总资产
        fundavl:可用余额
        daixiao:代销份额
        otc:OTC份额
        """
        return self._get_baseinfo()
    
    def _get_baseinfo(self):
        self.s.headers.update(vs.AGENT)
        txtdata = self.s.get(vs.BASE_URL % (vs.P_TYPE['https'], vs.DOMAINS['csc'], vs.PAGES['baseInfo']))
        jsonobj = utils.get_jdata(txtdata)
        stkdata = jsonobj['data']['moneytype0']
        stkdata['fundid'] = jsonobj['fundid']
        return pd.Series(stkdata)
    

    def check_login_status(self, return_data):
        if hasattr(return_data, 'get') and return_data.get('error_no') == '-1':
            raise NotLoginError
        
        
class NotLoginError(Exception):
    def __init__(self, result=None):
        super(NotLoginError, self).__init__()
        self.result = result
    def heartbeat(self):
        return self.baseinfo

