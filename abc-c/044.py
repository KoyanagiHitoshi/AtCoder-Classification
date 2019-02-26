#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
N,A=map(int,input().split())
X=[int(x)-A for x in input().split()]
combination=Counter([0])
for x in X:
    tmp=Counter()
    for key,count in combination.items():
        tmp[key+x]+=count
    combination+=tmp
print(combination[0]-1)
