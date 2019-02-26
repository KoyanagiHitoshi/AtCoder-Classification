#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=(int(input()) for _ in range(2))
x=[int(_) for _ in input().split()]
s=0
for i in range(len(x)):
    s+=min(x[i]*2,(k-x[i])*2)
print(s)
