#!/usr/bin/env python
# -*- conding: utf-8 -*-

import collections
import bisect
n,m=map(int,input().split())
p=[[int(j) for j in input().split()] for i in range(m)]
a=collections.defaultdict(list)
for x,y in sorted(p):
    a[x]+=[y]
for x,y in p:
    z=bisect.bisect(a[x],y)
    print("%06d%06d"%(x,z))
