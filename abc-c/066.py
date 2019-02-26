#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(N):
    B.append(A[i])
    B=B[::-1]
print(*B)
