'''
UnitTest for API
@author: Jimmy
'''
import unittest
#import tushare.stock.trading as td
import tushare.fund.nav as nav

class TestTrading(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2015-01-01'
        self.end = '2016-04-04'
    
    def test_tickData(self):
        self.set_data()        
        lst = []
        for item in lst:
            print 'get %s nav' %item
            df = nav.get_nav_open(item)
            print '\n','nums=',len(df),'\n',df[:2]

    def test_nav_history(self):
        self.set_data()
        lst = ['164905','161005','380007','000733','159920']        
        islst = [False,False,True,True,False]
        for k,item in enumerate(lst):
            print 'get %s nav' %item
            df = nav.get_nav_history(item,self.start,self.end,islst[k])
            if df is not None:
                print '\n','nums=',len(df),'\n',df[:2]
#     def test_histData(self):
#         self.set_data()
#         td.get_hist_data(self.code, start=self.start, end=self.end)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()