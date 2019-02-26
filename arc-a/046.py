#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
num=1
while N>0:
    if len(set(str(num)))==1:N-=1
    num+=1
print(num-1)


