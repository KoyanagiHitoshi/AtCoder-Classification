#!/usr/bin/env python
# -*- conding: utf-8 -*-

h,w=map(int,input().split())
a=[]
for i in range(h):
    x = input()
    if "#" in x:
        a.append(x)
a=list(zip(*a))
b=[]
for y in a:
    if "#" in y:
        b.append(y)
b=list(zip(*b))
for c in b:
    print("".join(c))

