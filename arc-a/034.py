#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
ans=0
for i in range(N):
    a,b,c,d,e=map(int,input().split())
    ans=max(ans,a+b+c+d+e*11/90)
print(ans)

