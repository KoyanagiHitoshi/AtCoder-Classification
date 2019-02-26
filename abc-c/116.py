#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
ans=0
base=0
for h in list(map(int,input().split())):
    ans+=max(0,h-base)
    base=h
print(ans)
