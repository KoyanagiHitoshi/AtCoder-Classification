#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=[(int(a), i) for i,a in enumerate(input().split(),1)]
for a in sorted(A,reverse=True):
    print(a[1])
