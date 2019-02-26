#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
for i in range(int(input())):
    l,r=map(int,input().split())
    s=s[:l-1]+s[l-1:r][::-1]+s[r:]
print(s)
