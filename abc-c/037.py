#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,K=map(int,input().split())
A=list(map(int,input().split()))
print(sum(sum(A[i:i+K]) for i in range(N-K+1)))
