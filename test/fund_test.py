# -*- coding:utf-8 -*- 

import unittest
import tushare.stock.fundamental as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2015-01-03'
        self.end = '2015-04-07'
        self.year = 2014
        self.quarter = 4

    def test_get_stock_basics(self):
        print(fd.get_stock_basics())
        
#     def test_get_report_data(self):
#         self.set_data()
#         print(fd.get_report_data(self.year, self.quarter))
#     
#     def test_get_profit_data(self):
#         self.set_data()
#         print(fd.get_profit_data(self.year, self.quarter))
#         
#     def test_get_operation_data(self):
#         self.set_data()
#         print(fd.get_operation_data(self.year, self.quarter))
#         
#     def test_get_growth_data(self):
#         self.set_data()
#         print(fd.get_growth_data(self.year, self.quarter))
#         
#     def test_get_debtpaying_data(self):
#         self.set_data()
#         print(fd.get_debtpaying_data(self.year, self.quarter))
#         
#     def test_get_cashflow_data(self):
#         self.set_data()
#         print(fd.get_cashflow_data(self.year, self.quarter))

if __name__ == '__main__':
    unittest.main()