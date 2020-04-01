import sys
import datetime
from unittest import TestCase


class Piecemeal(TestCase):
    def runTest(self):
        version = sys.version_info[0]
        today = datetime.datetime.today().date()
        print(type(today))
        assert version >= 3
