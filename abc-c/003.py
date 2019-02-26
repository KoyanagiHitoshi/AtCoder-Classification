#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,K=map(int,input().split())
R=sorted(map(int,input().split()))
score=0
for i in range(N-K,N):
    score=(score+R[i])/2
print(score)


