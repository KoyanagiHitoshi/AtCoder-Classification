#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
S=set(range(1,m+1))
for i in range(n):
    K,*A=map(int,input().split())
    S&=set(A)
print(len(S))
