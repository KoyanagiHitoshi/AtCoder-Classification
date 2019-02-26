#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
t=list(map(int,input().split()))
for i in range(int(input())):
    p,x=map(int,input().split())
    print(sum(t)-t[p-1]+x)
