#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
s=set()
for i in range(N):s^={input()}
print(len(s))
