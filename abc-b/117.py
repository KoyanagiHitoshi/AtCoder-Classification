#!/usr/bin/env python
# -*- conding: utf-8 -*-

int(input())
L=sorted(map(int,input().split()))[::-1]
print("Yes" if L[0]<sum(L[1:]) else "No")
