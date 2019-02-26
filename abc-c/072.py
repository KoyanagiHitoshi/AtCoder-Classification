#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
a=[0]*10**5
for i in map(int,input().split()):a[i]+=1
print(max(sum(a[i:i+3]) for i in range(10**5)))
