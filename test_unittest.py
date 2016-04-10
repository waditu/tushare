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
    
    def test_get_nav_open(self):
        self.set_data()        
        lst = ['all','equity','mix','bond','monetary','qdii']
        print '\nget nav ope................\n' 
        for item in lst:
            print 'get %s nav' %item
            df = nav.get_nav_open(item)
            print '\n','nums=',len(df),'\n',df[:2]

    def test_nav_history(self):
        self.set_data()
        lst = ['164905','161005','380007','000733','159920']        
        for k,item in enumerate(lst):
            print 'get %s nav' %item
            df = nav.get_nav_history(item,self.start,self.end)
            if df is not None:
                print '\n','nums=',len(df),'\n',df[:2]


    def test_get_fund_info(self):
        self.set_data()
        lst = ['164905','161005','380007','000733','159920']
        for item in lst:
            print 'get %s nav' %item
            df = nav.get_fund_info(item)
            if df is not None:
                print '%s fund info' %item,
                print df        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()