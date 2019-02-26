#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
two=four=0
for i in l:
    if i%4==0:four+=1
    elif i%2==0:two+=1
print("Yes" if two==n or four>=n//2 or two+2*four>=n else "No")
