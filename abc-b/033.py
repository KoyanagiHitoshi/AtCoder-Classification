#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
a=[]
l=[]
for i in range(n):
    s,p=input().split()
    a.append(s)
    l.append(int(p))
if max(l)>sum(l)/2:print(a[l.index(max(l))])
else:print("atcoder")



