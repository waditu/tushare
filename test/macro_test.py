# -*- coding:utf-8 -*-
'''
Created on 2015/01/24
@author: Jimmy Liu

Modified on 2020/06/28
@contributor: Cole ZHANG
@email: longzonejazz@gmail.com
'''
import unittest
import tushare.stock.macro as fd

class Test(unittest.TestCase):

    def test_get_gdp_year(self):
        print(fd.get_gdp_year())
              
    def test_get_gdp_quarter(self):
        print(fd.get_gdp_quarter())
         
    def test_get_gdp_for(self):
        print(fd.get_gdp_for())
     
    def test_get_gdp_pull(self):
        print(fd.get_gdp_pull())
         
    def test_get_gdp_contrib(self):
        print(fd.get_gdp_contrib())
         
    def test_get_cpi(self):
        print(fd.get_cpi())
         
    def test_get_ppi(self):
        print(fd.get_ppi())
         
    def test_get_loan_rate(self):
        print(fd.get_loan_rate())
         
    def test_get_rrr(self):
        print(fd.get_rrr())
         
    def test_get_money_supply(self):
        print(fd.get_money_supply())
          
    def test_get_money_supply_bal(self):
        print(fd.get_money_supply_bal())

    def test_get_total_import_export(self):
        print(fd.get_total_import_export())

    def test_get_industry_fixed_investment(self):
        print(fd.get_industry_fixed_investment())
        
        
if __name__ == "__main__":
    unittest.main()
