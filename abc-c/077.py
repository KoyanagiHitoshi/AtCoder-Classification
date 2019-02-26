#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
N=int(input())
A=Counter(input().split())
B=Counter(input().split())
C=Counter(input().split())
ans=0
for a_key,a_count in A.most_common():
    for b_key,b_count in B.most_common():
        for c_key,c_count in C.most_common():
            a_key,b_key,c_key=int(a_key),int(b_key),int(c_key)
            if a_key<b_key and b_key<c_key:
                ans+=a_count*b_count*c_count
print(ans)



