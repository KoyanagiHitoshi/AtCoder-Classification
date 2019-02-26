#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
s=input()
c,m=0,0
for i in range(len(s)):
    if s[i]=="I":
        c+=1
        m=max(c,m)
    if s[i]=="D":
        c=c-1
        m=max(c,m)
print(m)
