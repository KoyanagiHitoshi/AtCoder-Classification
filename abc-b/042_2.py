#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,l=map(int,input().split())
print(*sorted([input() for i in range(n)]),sep="")

