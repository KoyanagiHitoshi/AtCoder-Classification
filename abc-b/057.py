#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
a=[[int(j) for j in input().split()] for i in range(n)]
c=[[int(j) for j in input().split()] for i in range(m)]
for i in range(n):
    d=10e8
    b=0
    for j in range(m):
        if abs(a[i][0]-c[j][0])+abs(a[i][1]-c[j][1])<d:
            d=abs(a[i][0]-c[j][0])+abs(a[i][1]-c[j][1])
            b=j+1
    print(b)

