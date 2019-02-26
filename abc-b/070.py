#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c,d=map(int,input().split())
t=len(set(map(int,range(a,b+1)))&set(map(int,range(c,d+1))))-1
print("0" if t==-1 else t)
