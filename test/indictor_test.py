# -*- coding:utf-8 -*- 
'''
Created on 2018/05/26
@author: Jackie Liao
'''
import unittest
import tushare.stock.indictor as idx
import tushare as ts


class Test(unittest.TestCase):

    def test_plot_all(self):
        data = ts.get_k_data("601398", start="2018-01-01", end="2018-05-27")

        data = data.sort_values(by=["date"], ascending=True)

        idx.plot_all(data, is_show=True, output=None)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
