#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
l=sorted([int(_) for _ in input().split()])[::-1]
print(sum(l[i] for i in range(0,k)))

