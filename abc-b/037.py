#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,q=map(int,input().split())
a=[0]*n
for i in range(q):
    l,r,t=map(int,input().split())
    for i in range(l,r+1):a[i-1]=t
print(*a,sep="\n")
