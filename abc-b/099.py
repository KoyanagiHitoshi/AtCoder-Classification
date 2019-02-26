#!/usr/bin/env python
# -*- conding: utf-8 -*-

a, b = map(int, input().split())
n = b - a
print(n*(n+1)//2-b)
