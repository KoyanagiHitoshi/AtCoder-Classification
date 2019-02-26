#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
a=[input() for _ in range(n)]
b=[input() for _ in range(m)]
r=any([r[j:j+m] for r in a[i:i+m]]==b for i in range(n-m+1) for j in range(n-m+1))
print('Yes' if r else 'No')
