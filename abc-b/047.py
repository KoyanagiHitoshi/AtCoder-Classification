#!/usr/bin/env python
# -*- conding: utf-8 -*-

w,h,n=map(int,input().split())
l=[[int(j) for j in input().split()] for i in range(n)]
b=c=0
d=w
e=h
for i in range(n):
    a=l[i][2]
    if a==1:b=max(b,l[i][0])
    if a==2:d=min(d,l[i][0])
    if a==3:c=max(c,l[i][1])
    if a==4:e=min(e,l[i][1])
print([(d-b)*(e-c),0][(d<b)|(e<c)])
