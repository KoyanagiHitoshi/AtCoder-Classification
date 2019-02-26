#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
a=(n//k)**3
if k%2==0:
    n+=k//2
    a+=(n//k)**3
print(a)
