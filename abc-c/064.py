#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
color=[0]*8
free=0
for a in A:
    if 1<=a<=399:color[0]=1
    elif 400<=a<=799:color[1]=1
    elif 800<=a<1199:color[2]=1
    elif 1200<=a<=1599:color[3]=1
    elif 1600<=a<=1999:color[4]=1
    elif 2000<=a<=2399:color[5]=1
    elif 2400<=a<=2799:color[6]=1
    elif 2800<=a<=3199:color[7]=1
    elif 3200<=a<=4800:free+=1
M=sum(color)+free
m=1 if sum(color)==0 and free!=0 else sum(color)
print(m,M)
