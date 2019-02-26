#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
k=int(input())
s=1
for i in range(n):s=min(s*2,s+k)
print(s)
