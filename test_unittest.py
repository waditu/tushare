'''
UnitTest for API
@author: Jimmy
'''
import unittest
import tushare.stock.trading as td

class TestTrading(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2014-11-03'
        self.end = '2014-11-07'
    
    def test_tickData(self):
        self.set_data()
        td.get_tick_data(self.code, date=self.start)
    
#     def test_histData(self):
#         self.set_data()
#         td.get_hist_data(self.code, start=self.start, end=self.end)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()