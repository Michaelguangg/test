# -*- coding: utf-8 -*-
#!/usr/bin/python
#test_copyfile.py

import os,shutil
import datetime
import time

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

def gettoday():
    today=datetime.date.today()  
    strdate=today.strftime('%Y%m%d')
    return strdate
def getyestoday():
    today=datetime.date.today()  
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday 
    strdate=yesterday.strftime('%Y%m%d')
    return strdate
strdate=getyestoday()
srcfile=r'xxx.xlsx'
dstfile=r'xxx-%s.xlsx'%(strdate)
print(srcfile)
print(dstfile)
mycopyfile(srcfile,dstfile)
time.sleep(2)