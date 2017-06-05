
import unittest
import tushare as ts


class Test(unittest.TestCase):
    def test_grab_from_sz_replied(self):
        df = ts.investor_relations.grab_from_sz_replied("000001")
        df.to_csv("SZ000001_replied.csv", encoding="utf-8")

    def test_grab_from_sz_all(self):
        df = ts.investor_relations.grab_from_sz_all("000001")
        df.to_csv("SZ000001_all.csv", encoding="utf-8")

    def test_grab_from_sh_replied(self):
        df = ts.investor_relations.grab_from_sh_replied("601398")
        df.to_csv("SH601398_replied.csv", encoding="utf-8")

    def test_grab_from_sh_unreplied(self):
        df = ts.investor_relations.grab_from_sh_unreplied("601398")
        df.to_csv("SH601398_unreplied.csv", encoding="utf-8")

if __name__ == "__main__":
    unittest.main()