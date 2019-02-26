#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
ans=0
for i in range(N):
    x,u=input().split()
    if u=="BTC":ans+=float(x)*380000
    else:ans+=int(x)
print(ans)
