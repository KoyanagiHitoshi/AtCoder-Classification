#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
T=sorted(int(input()) for i in range(N))[::-1]
x=y=0
for t in T:
    if x<y:x+=t
    else:y+=t
print(max(x,y))

