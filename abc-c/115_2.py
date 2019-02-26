#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
h=sorted([int(input()) for i in range(n)])
print(min(h[i+k-1]-h[i] for i in range(n-k+1)))

