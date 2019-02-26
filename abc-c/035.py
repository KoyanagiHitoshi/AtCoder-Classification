#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,Q=map(int,input().split())
O=[0]*N
for i in range(Q):
    l,r=map(int,input().split())
    for j in range(l,r+1):
        O[j-1]+=1
for i in range(N):
    if O[i]%2==0:
        O[i]=0
    else:
        O[i]=1
print(*O,sep="")
