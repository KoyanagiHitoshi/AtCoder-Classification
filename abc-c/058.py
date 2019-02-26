#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
n=int(input())
s=Counter(input())
for i in range(n-1):
    s&=Counter(input())
print("".join(sorted(s.elements())))

