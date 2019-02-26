#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
s=input()
c,m=0,0
for i in range(len(s)):
    if s[i]=="I":c,m=c+1,max(c,m)
    if s[i]=="D":c,m=c-1,max(c,m)
print(m)
