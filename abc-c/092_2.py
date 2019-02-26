#!/usr/bin/env python
# -*- conding: utf-8 -*-


N=int(input())
A=[0]+list(map(int,input().split()))+[0]
cost=sum(abs(A[i+1]-A[i]) for i in range(N+1))
for i in range(1,N+1):
    print(cost-abs(A[i+1]-A[i])-abs(A[i]-A[i-1])+abs(A[i+1]-A[i-1]))

