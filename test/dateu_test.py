# -*- coding:utf-8 -*-
"""
@author: ZackZK
"""

from unittest import TestCase

from tushare.util import dateu
from tushare.util.dateu import is_holiday


class Test_Is_holiday(TestCase):
    def test_is_holiday(self):
        dateu.holiday = ['2016-01-04']  # holiday stub for later test
        self.assertTrue(is_holiday('2016-01-04'))  # holiday
        self.assertFalse(is_holiday('2016-01-01'))  # not holiday
        self.assertTrue(is_holiday('2016-01-09'))  # Saturday
        self.assertTrue(is_holiday('2016-01-10'))  # Sunday

