#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Created on 2015年7月4日
@author: JimmyLiu
@QQ:52799046
"""

try:
    from httplib import HTTPSConnection
except ImportError:
    from http.client import HTTPSConnection
import urllib

HTTP_OK = 200
HTTP_AUTHORIZATION_ERROR = 401

class Client:
    domain = 'api.wmcloud.com'
    port = 443
    token = ''
    httpClient = None
    def __init__(self , token):
        self.token = token
        self.httpClient = HTTPSConnection(self.domain, self.port)
        
    def __del__( self ):
        if self.httpClient is not None:
            self.httpClient.close()
            
    def encodepath(self, path):
        start=0
        n=len(path)
        re=''
        i=path.find('=', start)
        while i!=-1 :
            re+=path[start:i+1]
            start=i+1
            i=path.find('&', start)
            if(i>=0):
                for j in range(start, i):
                    if(path[j]>'~'):
                        re+=urllib.quote(path[j])
                    else:
                        re+=path[j]  
                re+='&'
                start=i+1
            else:
                for j in range(start, n):
                    if(path[j]>'~'):
                        re+=urllib.quote(path[j])
                    else:
                        re+=path[j]  
                start=n
            i=path.find('=', start)
        return re
    
    
    def init(self, token):
        self.token=token
        
        
    def getData(self, path):
        result = None
        path='/data/v1'+path
        path=self.encodepath(path)
        try:
            self.httpClient.request('GET', path, headers = {"Authorization": "Bearer " + self.token})
            response = self.httpClient.getresponse()
            if response.status == HTTP_OK:
                result = response.read()
            else:
                result = response.read()
            if(path.find('.csv?')!=-1):
                result=result.decode('GBK').encode('utf-8')
            return response.status, result
        except Exception as e:
            raise e
        return -1, result
