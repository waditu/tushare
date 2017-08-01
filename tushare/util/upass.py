# -*- coding:utf-8 -*- 

"""
Created on 2015/08/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import pandas as pd
import os
from tushare.stock import cons as ct

BK = 'bk'

def set_token(token):
    df = pd.DataFrame([token], columns=['token'])
    df.to_csv(ct.TOKEN_F_P, index=False)
    
    
def get_token():
    if os.path.exists(ct.TOKEN_F_P):
        df = pd.read_csv(ct.TOKEN_F_P)
        return str(df.ix[0]['token'])
    else:
        print(ct.TOKEN_ERR_MSG)
        return None


def set_broker(broker='', user='', passwd=''):
    df = pd.DataFrame([[broker, user, passwd]], 
                      columns=['broker', 'user', 'passwd'],
                      dtype=object)
    if os.path.exists(BK):
        all = pd.read_csv(BK, dtype=object)
        if (all[all.broker == broker]['user']).any():
            all = all[all.broker != broker]
        all = all.append(df, ignore_index=True)
        all.to_csv(BK, index=False)
    else:
        df.to_csv(BK, index=False)
        
        
def get_broker(broker=''):
    if os.path.exists(BK):
        df = pd.read_csv(BK, dtype=object)
        if broker == '':
            return df
        else:
            return  df[df.broker == broker]
    else:
        return None
    
    
def remove_broker():
    os.remove(BK)
