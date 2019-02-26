#!/usr/bin/env python
# -*- conding: utf-8 -*-

import bisect
N,K=map(int,input().split())
l=[]
for i in range(N):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
count=0
for a,b in l:
    count+=b
    if K<=count:
        print(a)
        break
