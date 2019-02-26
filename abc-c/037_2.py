#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,K=map(int,input().split())
A=list(map(int,input().split()))
print(sum(A[i]*min(i+1,K,N-i,N-K+1) for i in range(N)))
