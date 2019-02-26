#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
l=" ".join([input() for _ in [0]*m])
for i in range(1,n+1):print(l.split().count(str(i)))
