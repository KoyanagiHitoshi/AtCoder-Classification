#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=[int(input()) for _ in range(n)]
s=list(set(l))
c=0
for i in range(len(s)):
    t=l.count(s[i])
    if t>1:
        c+=t-1
print(c)
