#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,K=map(int,input().split())
S=[int(input()) for i in range(N)]
length=0
if 0 in S:
    length=N
else:
    for i in range(N):
        for j in range(i+1,N):
            mul=1
            for k in range(i,j+1):
                mul*=S[k]
            if mul<=K:
                length=max(length,j-i+1)
print(length)


