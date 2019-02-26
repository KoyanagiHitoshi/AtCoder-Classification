#!/usr/bin/env python
# -*- conding: utf-8 -*-

import itertools
N,K=map(int,input().split())
S={0}
for i in range(N):S=set.union(*[{int(k)^s for s in S} for k in input().split()])
if 0 in S:print("Found")
else:print("Nothing")
