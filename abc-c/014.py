#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
n=10**6+1
x=[0]*(n+1)
for i in range(N):
    a,b=map(int,input().split())
    x[a]+=1
    x[b+1]-=1
for i in range(n):
    x[i+1]+=x[i]
print(max(x))

