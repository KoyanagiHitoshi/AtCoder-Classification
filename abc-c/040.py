#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))+[0]
dp=[0]*N
dp[1]=abs(A[1]-A[0])
for i in range(1,N-1):
    dp[i+1]=min(dp[i]+abs(A[i+1]-A[i]),dp[i-1]+abs(A[i+1]-A[i-1]))
print(dp[N-1])
