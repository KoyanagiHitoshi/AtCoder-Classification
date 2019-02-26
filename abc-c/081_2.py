#!/usr/bin/env python
# -*- conding: utf-8 -*-

from collections import Counter
n,k=map(int,input().split())
a=Counter(input().split())
print(sum(sorted(a.values(),reverse=True)[k:]))
