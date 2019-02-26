#!/usr/bin/env python
# -*- conding: utf-8 -*-

XU=[input().split() for i in range(int(input()))]
print(sum([float(x)*{"JPY":1,"BTC":380000}[u] for x,u in XU]))
