#!/usr/bin/env python
# -*- conding: utf-8 -*-

from itertools import combinations
from collections import Counter
N=int(input())
S=Counter()
for i in range(N):
    S[input()[0]]+=1
print(sum([S[a]*S[b]*S[c] for a,b,c in combinations("MARCH",3)]))
