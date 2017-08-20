TUSHARE_UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
def get_ua():
    return TUSHARE_UA

def set_ua(user_agent):
    TUSHARE_UA={'User-Agent':user_agent}
