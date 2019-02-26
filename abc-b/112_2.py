#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,T=map(int,input().split())
m=1001
for i in range(N):
    c,t=map(int,input().split())
    if t<=T:m=min(m,c)
print("TLE" if m==1001 else m)
