# -*- coding:utf-8 -*- 

import tushare.stock.newsevent as ns

if __name__ == '__main__':
    df = ns.get_latest_news(2,show_content=True)
    print df
    
    url = df.ix[0,'url']
    print ns.latest_content(url)