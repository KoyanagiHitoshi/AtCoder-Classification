#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
k=int(input())
print(sum(min(x,k-x)*2 for x in map(int,input().split())))
