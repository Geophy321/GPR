# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:52:15 2019

@author: gqs
"""
import os
import struct
import numpy as np
#import matplotlib.pyplot as plt
def floatprcss():
    while f.read(1):
        f.seek(-1,os.SEEK_CUR)
        for i in range(7):
            tmp=f.read(4)
            info[i]=struct.unpack("i",tmp)[0]
            #print(info[i],i)

        trcnmb=info[0]#print(sample)
        sample=info[1]#print(trcnmb)
        trmk=f.read(2)
        trtm=f.read(4)
        tmdly=f.read(4)
        for j in range(9):
            tmp=f.read(8)
            dblinfo[j]=struct.unpack("d",tmp)[0]
            #print(dblinfo[j])
    
        trcgn=f.read(4)
        tmcllt=f.read(8)
        for j in range(8):
            tmp=f.read(4)
            dummy[j]=struct.unpack("f",tmp)[0]
            #print(dummy[j])
        tmp=f.read(4)
        for i in range(sample):
            trcdt=f.read(4)
            #tracedata=struct.unpack("f",trcdt)[0]
            #print(tracedata)

    print("the trace number is",trcnmb)
    print("the sample number is",sample)
    tracedat=np.zeros(sample,dtype='f')
    tracedata=np.zeros(sample,dtype='f')
    f.seek(0,0)
    for i in range(trcnmb):
        for j in range(79):
            tmp=f.read(2)
            fw.write(tmp)
        
        for m in range(sample):
            trcdt=f.read(4)
            tracedata[m]=struct.unpack("f",trcdt)[0]
            #print(tracedata[i][j]
    
        for m in range(sample):
            temp_attri = 0
            num_pos =0
            if m<tm_win:
                for k in range(m+1+tm_win):
                    if tracedata[k]>0:
                        temp_attri=temp_attri+tracedata[k]
                        num_pos=num_pos+1
                    
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                    
        
            if m>=tm_win and m<=sample-tm_win-1:
                for k in range(tm_win*2+1):
                    if tracedata[m-tm_win+k]>0:
                        temp_attri=temp_attri+tracedata[m-tm_win+k]
                        num_pos=num_pos+1
                    
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                    
       
            else:
                for k in range(tm_win+1+sample-m-1):
                    if tracedata[m-tm_win+k]>0:
                        temp_attri=temp_attri+tracedata[m-tm_win+k]
                        num_pos=num_pos+1
                   
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                   
                   
        fw.write(tracedat)
        print(i)
    

def intprcss():
    while f.read(1):
        f.seek(-1,os.SEEK_CUR)
        for i in range(7):
            tmp=f.read(4)
            info[i]=struct.unpack("i",tmp)[0]
            #print(info[i],i)

        trcnmb=info[0]
        sample=info[1]
        #print(trcnmb)
        #print(sample)
        trmk=f.read(2)
        trtm=f.read(4)
        tmdly=f.read(4)
        for j in range(9):
            tmp=f.read(8)
            dblinfo[j]=struct.unpack("d",tmp)[0]
            #print(dblinfo[j])
    
        trcgn=f.read(4)
        tmcllt=f.read(8)
        for j in range(8):
            tmp=f.read(4)
            dummy[j]=struct.unpack("f",tmp)[0]
            #print(dummy[j])
        tmp=f.read(2)
        for i in range(sample):
            trcdt=f.read(2)
            #tracedata=struct.unpack("h",trcdt)[0]
            #print(tracedata)

    print('the trace number is',trcnmb)
    print('the sample number is',sample)
    tracedat=np.zeros(sample,dtype='int16')
    tracedata=np.zeros(sample,dtype='int16')
    f.seek(0,0)
    for i in range(trcnmb):
        for j in range(78):
            tmp=f.read(2)
            fw.write(tmp)
        
        for m in range(sample):
            trcdt=f.read(2)
            tracedata[m]=struct.unpack("h",trcdt)[0]
            #print(tracedata[i][j]
    
        for m in range(sample):
            temp_attri = 0
            num_pos =0
            if m<tm_win:
                for k in range(m+1+tm_win):
                    if tracedata[k]>0:
                        temp_attri=temp_attri+tracedata[k]
                        num_pos=num_pos+1
                    
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                    
        
            if m>=tm_win and m<=sample-tm_win-1:
                for k in range(tm_win*2+1):
                    if tracedata[m-tm_win+k]>0:
                        temp_attri=temp_attri+tracedata[m-tm_win+k]
                        num_pos=num_pos+1
                    
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                    
       
            else:
                for k in range(tm_win+1+sample-m-1):
                    if tracedata[m-tm_win+k]>0:
                        temp_attri=temp_attri+tracedata[m-tm_win+k]
                        num_pos=num_pos+1
                   
                    if num_pos>0:
                        tracedat[m]=temp_attri/num_pos
                   
                   
        fw.write(tracedat)
        print(i)



if __name__=="__main__":
    i=0
    j=0
    tm_win=3
    info=np.zeros(7,dtype=int)
    dblinfo=np.zeros(9,dtype=float)
    dummy=np.zeros(8,dtype='f')
    flag='float'
    f=open(r'D:\Yawargprdata\processed\2017\11_03_2017\106\PROCDATA\YP000000.05T','rb')
    fh=open(r'D:\Yawargprdata\processed\2017\11_03_2017\106\PROCDATA\YP000000.05R','rb')
    fhw=open(r'D:\Yawargprdata\processed\2017\11_03_2017\106\PROCDATA\YPampaver.05R','wb')
    fw=open(r'D:\Yawargprdata\processed\2017\11_03_2017\106\PROCDATA\YPampaver.05T','wb')
    while fh.read(1):
        fh.seek(-1,os.SEEK_CUR)
        tp=fh.read(1)
        fhw.write(tp)

    fh.close()
    fhw.close()
    if(flag=="int"):
        intprcss()
    
    if(flag=="float"):
        floatprcss()
       
    f.close()
    fw.close()





