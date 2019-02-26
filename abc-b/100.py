#!/usr/bin/env python
# -*- conding: utf-8 -*-

d,n=map(int,input().split())
l=[int(pow(100,d)*i) for i in range(1,n+2)]
print(l[n-1])

