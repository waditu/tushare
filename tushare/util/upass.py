# -*- coding:utf-8 -*- 

"""
通联数据token设置
Created on 2015/08/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import pandas as pd
import os
from tushare.stock import cons as ct

def set_token(token):
    df = pd.DataFrame([token], columns={'token'})
    df.to_csv(ct.TOKEN_F_P, index=False)
    
    
def get_token():
    if os.path.exists(ct.TOKEN_F_P):
        df = pd.read_csv(ct.TOKEN_F_P)
        return str(df.ix[0]['token'])
    else:
        print(ct.TOKEN_ERR_MSG)
        return None

 
