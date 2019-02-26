#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,l=map(int,input().split())
s=sorted([input() for i in range(n)])
print(*s,sep="")

