#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=input()
A=list(map(int,input().split()))
ans=0
for a in A:
    ans+=a-1
print(ans)
