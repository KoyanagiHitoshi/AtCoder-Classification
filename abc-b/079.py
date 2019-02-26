#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=[2,1]
for i in range(2,n+3):
    l.append(l[i-2]+l[i-1])
print(l[n])
