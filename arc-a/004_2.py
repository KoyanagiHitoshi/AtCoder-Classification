#!/usr/bin/env python
# -*- conding: utf-8 -*-

p=[list(map(int,input().split())) for i in range(int(input()))]
print(max(((a[0]-b[0])**2+(a[1]-b[1])**2)**.5 for b in p for a in p))
