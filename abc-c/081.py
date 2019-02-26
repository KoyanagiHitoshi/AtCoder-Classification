#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
n,k=map(int,input().split())
a=Counter(input().split())
ans=0
keys,counts=zip(*a.most_common())
for num,(key,count) in enumerate(zip(keys,counts)):
    if int(num)>k-1:ans+=count
print(ans)
