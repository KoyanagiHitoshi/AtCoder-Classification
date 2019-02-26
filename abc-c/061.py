#!/usr/bin/env python
# -*- conding: utf-8 -*-

import bisect
N,K=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    for i in range(b):
        B.append(a)
print(B[K-1])
