#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
print(min(abs(sum(A[:i])-sum(A[i:])) for i in range(1,N)))
