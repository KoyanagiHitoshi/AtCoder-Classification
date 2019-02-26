#!/usr/bin/env python
# -*- conding: utf-8 -*-

from fractions import gcd
def lcm(a,b): return a*b//gcd(a,b)
N=int(input())
T=[int(input()) for i in range(N)]
ans=1
for t in T:
    ans=lcm(ans,t)
print(ans)
