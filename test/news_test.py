# -*- coding:utf-8 -*- 

import tushare.stock.newsevent as ns

if __name__ == '__main__':
    df = ns.get_latest_news(5,show_content=False)
    print df
     
#     url = df.ix[0,'url']
#     print ns.latest_content(url)

#    nts = ns.get_notices('600848')
# #    print nts
#    url = nts.ix[0,'url'] 
#    print ns.notice_content(url)