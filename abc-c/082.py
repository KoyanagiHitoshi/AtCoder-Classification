#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
n=int(input())
a=Counter(input().split())
count=0
keys,counts=zip(*a.most_common())
for i,j in zip(keys,counts):
    i=int(i)
    if i>j:
        count+=j
    elif i<j:
        count+=j-i
print(count)
