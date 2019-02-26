#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
i=int(N**(1/2))
while N%i!=0:
    i-=1
print(len(str(N//i)))
