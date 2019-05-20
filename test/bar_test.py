# -*- coding:utf-8 -*- 
'''
Created on 2017/9/24
@author: Jimmy Liu
'''
import unittest
import tushare.stock.trading as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = ''
        self.end = ''
        
    def test_bar_data(self):
        self.set_data()
        print(fd.bar(self.code, self.start, self.end))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()