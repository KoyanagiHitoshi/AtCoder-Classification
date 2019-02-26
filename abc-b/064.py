#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
l=sorted(set(map(int,input().split())))
print(max(l)-min(l))
