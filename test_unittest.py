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
        print '\nget nav open................\n' 
        for item in lst:
            print 'get %s nav' %item
            df = nav.get_nav_open(item)
            print '\n','nums=',len(df),'\n',df[:2]


    def test_get_nav_close(self):
        self.set_data()        
        t2 = ['all','fbqy','fbzq']
        qy_t3 = ['all','ct','cx']
        zq_t3 = ['all','wj','jj','cz']

        print '\nget nav closed................\n' 
        df = None
        for item in t2:
            if item == 'fbqy':
                for t3i in qy_t3:
                    print 'get %s-%s nav' %(item,t3i)
                    df = nav.get_nav_close(item,t3i)
                    print '\n','nums=',len(df),'\n',df[:2] 
            elif item == 'fbzq':
                for t3i in zq_t3:
                    print 'get %s-%s nav' %(item,t3i)
                    df = nav.get_nav_close(item,t3i)
                    print '\n','nums=',len(df),'\n',df[:2] 
            else:
                print 'get %s nav' %item
                df = nav.get_nav_close(item)
                print '\n','nums=',len(df),'\n',df[:2] 

    def test_get_nav_grading(self):
        self.set_data()        
        t2 = ['all','fjgs','fjgg']        
        t3 = {'all':'0','wjzq':'13','gp':'14','zs':'15','czzq':'16','jjzq':'17'}

        print '\nget nav grading................\n' 
        df = None
        for item in t2:
            if item == 'all':
                print 'get %s nav' %item
                df = nav.get_nav_grading(item)
                print '\n','nums=',len(df),'\n',df[:2] 
            else:
                for t3i in t3.keys():
                    print 'get %s-%s nav' %(item,t3i)
                    df = nav.get_nav_grading(item,t3i)     
                    print '\n','nums=',len(df),'\n',df[:2]                                    

    def test_nav_history(self):
        self.set_data()
        lst = ['164905','161005','380007','000733','159920','164902','184721','165519','164302','519749','150275','150305','150248']
        for k,item in enumerate(lst):
            print 'get %s nav' %item
            df = nav.get_nav_history(item,self.start,self.end)
            if df is not None:
                print '\n','nums=',len(df),'\n',df[:2]


    def test_get_fund_info(self):
        self.set_data()
        lst = ['164905','161005','380007','000733','159920','164902','184721','165519','164302','519749','150275','150305','150248']
        for item in lst:
            print 'get %s nav' %item
            df = nav.get_fund_info(item)
            if df is not None:
                print '%s fund info' %item,
                print df        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()