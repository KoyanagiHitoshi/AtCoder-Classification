#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,D,K=map(int,input().split())
LR=[list(map(int,input().split())) for i in range(D)]
ST=[list(map(int,input().split())) for i in range(K)]
for s,t in ST:
    ans=0
    for l,r in LR:
        ans+=1
        if l<=t<=r and l<=s<=r:
            print(ans)
            break
        if l<=s<=r:
            if abs(t-r)<abs(t-l):s=r
            else:s=l
