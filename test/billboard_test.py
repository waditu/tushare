# -*- coding:utf-8 -*-
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
import tushare.stock.billboard as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.date = '2015-06-12'
        self.days = 5

    def test_top_list(self):
        self.set_data()
        print(fd.top_list(self.date))

    def test_cap_tops(self):
        self.set_data()
        print(fd.cap_tops(self.days))

    def test_broker_tops(self):
        self.set_data()
        print(fd.broker_tops(self.days))

    def test_inst_tops(self):
        self.set_data()
        print(fd.inst_tops(self.days))

    def test_inst_detail(self):
        print(fd.inst_detail())

    def test_get_em_xuangu(self):
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[gz01(4|2,5|10)]&p=1&jn=bRcdkFLB&ps=40&s=gz01(4|2,5|10)&st=1&r=1495853526526'
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK0685)]&p=1&jn=XMlOhJak&ps=40&s=gfzs7(BK0685)&st=1&r=1495858108749'
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[hqzb06(1|10)]&p=1&jn=nTiaCPKx&ps=40&s=hqzb06(1|10)&st=-1&r=1495858916202'
        args = 'type=xgq&sty=xgq&token=eastmoney&c=[hqzb06(1|10)][gz01(1|0.5)]&p=1&jn=bbANYnOi&ps=40&s=gz01(1|0.5)&st=-1&r=1495859000981'
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK0685)]&p=3&jn=gHTyZcgx&ps=40&s=gfzs7(BK0685)&st=1&r=1495872577477'
        args = 'type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK0685)][gfzs7(BK0701)]&p=1&jn=eGESMvPI&ps=40&s=gfzs7(BK0701)&st=1&r=1495873571656'
        args = 'type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK0701)]&p=1&jn=miupWSAg&ps=40&s=gfzs7(BK0701)&st=1&r=1495873611908'
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK0505)]&p=1&jn=PyAUJluU&ps=40&s=gfzs7(BK0505)&st=1&r=1495874071329'
        # args = 'type=xgq&sty=xgq&token=eastmoney&c=[gz01(1|0)]&p=70&jn=ppTbgXzs&ps=40&s=gz01(1|0)&st=-1&r=1495874145609'
        print(fd.get_em_xuangu(args))

if __name__ == "__main__":
    unittest.main()
