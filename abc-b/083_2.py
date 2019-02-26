#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,a,b=map(int,input().split())
s=0
for i in range(n+1):
    if a<=sum(int(j) for j in str(i))<=b:
        s+=i
print(s)
