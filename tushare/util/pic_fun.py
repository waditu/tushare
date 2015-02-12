# -*- coding:utf-8 -*- 

import numpy as np
import pandas as pd
from PIL import Image
import subprocess
    
def pic_cvt():
    from StringIO import StringIO
    import requests
    res = requests.get('https://investorservice.cfmmc.com/veriCode.do')
#     res = requests.get('http://jgsb.agri.gov.cn/yzm/random.jsp')
#     res = requests.get('https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&')
    img = Image.open(StringIO(res.content))
    
#     img = Image.open('c:/12.png')
    img = img.convert('RGB')
    pixdata = img.load()
    
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    
    img.save('c:/q3.bmp')

    im = img.convert('1')
    width,height = im.size
    print width,height
    data = im.load()
    
    nd = []
    for y in range(height):
        rd = []
        for x in range(width):
            rd.append(data[x,y])
        nd.append(rd)
    nd = np.asarray(nd)
    df = pd.DataFrame(nd)
    df[df==255] = 1
    
    rowc = []
    for c in df.columns:
        rowc.append([c,np.sum(df[c])])
    
    for d in rowc:
        if d[1]<3:
            for y in range(height):
                data[int(d[0]),y] = 0
    
    rowi = []
    for i in df.index:
        rowi.append([i,np.sum(df.ix[i])])
    
    for ir in rowi:
        if ir[1] < 7:
            for x in range(width):
                data[x,int(ir[0])] = 0
            
    im.save('c:/myt.bmp')
    
    proc = subprocess.Popen('tesseract c:/myt.bmp c:/res -l eng -psm 6',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    errors = proc.stdout.read()
    status, errors = proc.wait(), errors
    if status:
            print 'err'
    else:
        print open('c:/res.txt').readlines()[0]

if __name__ == '__main__':
    pic_cvt()
