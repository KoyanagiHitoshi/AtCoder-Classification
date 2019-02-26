#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
d,x=map(int,input().split())
for i in range(n):
    a=int(input())
    x+=(d+a-1)//a
print(x)

