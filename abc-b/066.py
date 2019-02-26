#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
for i in range(1,len(s)):
    t=s[:len(s)-i]
    if t[len(t)//2:]==t[:len(t)//2]:
        print(len(t))
        exit()
