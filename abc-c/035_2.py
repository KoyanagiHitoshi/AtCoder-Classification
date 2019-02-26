#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,Q=map(int,input().split())
O=[0]*(N+1)
for i in range(Q):
    l,r=map(int,input().split())
    O[l-1]+=1
    O[r]-=1
for i in range(N):
    if i>0:O[i]+=O[i-1]
    print(O[i]%2,end="")
print()
