#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,x=map(int,input().split())
A=list(map(int,input().split()))+[0]
ans=0
for i in range(N):
    eated=max(0,A[i]+A[i-1]-x)
    ans+=eated
    A[i]-=eated
print(ans)
