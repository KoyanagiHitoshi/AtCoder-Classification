#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
C=[int(input()) for i in range(N)]
count=[0]*N
for i in range(N):
    for j in range(N):
        if C[j]%C[i]==0:count[j]+=1
expect=[0]*N
for i in range(N):
    expect[i]=(count[i]+1)//2/count[i]
print(sum(expect))
