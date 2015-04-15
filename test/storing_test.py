# -*- coding:utf-8 -*- 

import os
from sqlalchemy import create_engine
from pandas.io.pytables import HDFStore
import tushare as ts

def csv():
    df = ts.get_hist_data('000875')
    df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])

def xls():
    df = ts.get_hist_data('000875')
    #直接保存
    df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)

def hdf():
    df = ts.get_hist_data('000875')
#     df.to_hdf('c:/day/store.h5','table')
    
    store = HDFStore('c:/day/store.h5')
    store['000875'] = df
    store.close()

def json():
    df = ts.get_hist_data('000875')
    df.to_json('c:/day/000875.json',orient='records')

    #或者直接使用
    print(df.to_json(orient='records'))

def appends():
    filename = 'c:/day/bigfile.csv'
    for code in ['000875', '600848', '000981']:
        df = ts.get_hist_data(code)
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=None)
        else:
            df.to_csv(filename)  

def db():
    df = ts.get_tick_data('600848',date='2014-12-22')
    engine = create_engine('mysql://root:jimmy1@127.0.0.1/mystock?charset=utf8')
#     db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='jimmy1',db="mystock",charset="utf8")
#     df.to_sql('TICK_DATA',con=db,flavor='mysql')
#     db.close()
    df.to_sql('tick_data',engine,if_exists='append')

def nosql():
    import pymongo
    import json
    conn = pymongo.Connection('127.0.0.1', port=27017)
    df = ts.get_tick_data('600848',date='2014-12-22')
    print(df.to_json(orient='records'))
    
    conn.db.tickdata.insert(json.loads(df.to_json(orient='records')))
    
#     print conn.db.tickdata.find()
    
if __name__ == '__main__':
    nosql()