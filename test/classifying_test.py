# -*- coding:utf-8 -*- 
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
import tushare.stock.classifying as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2015-01-03'
        self.end = '2015-04-07'
        self.year = 2014
        self.quarter = 4
        
    def test_get_industry_classified(self):
        print(fd.get_industry_classified())
        
    def test_get_concept_classified(self):
        print(fd.get_concept_classified())
        
    def test_get_area_classified(self):
        print(fd.get_area_classified())
        
    def test_get_gem_classified(self):
        print(fd.get_gem_classified())
        
    def test_get_sme_classified(self):
        print(fd.get_sme_classified())
        
    def test_get_st_classified(self):
        print(fd.get_st_classified())
    
    def test_get_hs300s(self):
        print(fd.get_hs300s())   
        
    def test_get_sz50s(self):
        print(fd.get_sz50s()) 
      
    def test_get_zz500s(self):
        print(fd.get_zz500s())   
        
if __name__ == "__main__":
    unittest.main()
    
#     suite = unittest.TestSuite()  
#     suite.addTest(Test('test_get_gem_classified'))  
#     unittest.TextTestRunner(verbosity=2).run(suite)
