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

    def test_get_em_gdzjc(self):
        self.set_data()
        print(fd.get_em_gdzjc(1, '2017-05-10', '2017-05-15'))
        print(fd.get_em_gdzjc())
        print(fd.get_em_gdzjc(1))
        print(fd.get_em_gdzjc(0))

if __name__ == "__main__":
    unittest.main()
