#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,a,b=map(int,input().split())
x=0
for i in range(n):
    s,d=input().split()
    d=int(d)
    if s=="East":
        if d<a:d=a
        if d>b:d=b
    else:
        if d<a:d=a
        if d>b:d=b
        d=-d
    x+=d
print("0" if x==0 else "East "+str(x) if x>0 else "West "+str(abs(x)))


