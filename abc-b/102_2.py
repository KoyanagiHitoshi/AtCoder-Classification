#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = input()
s = 0
for n in N:
    s += int(n)
print("Yes" if int(N)%s==0 else "No") 
