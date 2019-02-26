#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=[1,2,4,8,16,32,64]
m=0
for i in l:
    if i <= n:
        m=max(m,i)
print(m)
