#!/usr/bin/env python
# -*- conding: utf-8 -*-

from fractions import gcd
def lcm(a,b): return a*b//gcd(a,b)
N=int(input())
ans=1
for i in range(N):
    t=int(input())
    ans=lcm(ans,t)
print(ans)
