#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
l=sorted(map(int,input().split()))[::-1]
print(sum(l[::2])-sum(l[1::2]))
