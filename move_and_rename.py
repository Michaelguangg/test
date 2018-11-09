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
        fpath,fname=os.path.split(dstfile)    #�����ļ�����·��
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #����·��
        shutil.move(srcfile,dstfile)          #�ƶ��ļ�
        print("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #�����ļ�����·��
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #����·��
        shutil.copyfile(srcfile,dstfile)      #�����ļ�
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