#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(max(sum(a[:i+1])+sum(b[i:]) for i in range(n)))

