#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,x=map(int,input().split())
A=list(map(int,input().split()))+[0]
ans=0
for i in range(N):
    if A[i]+A[i+1]>x:
        eat=A[i+1]+A[i]-x
        if eat>A[i+1] and eat>A[i]:
            if A[i]>A[i+1]:
                A[i]=0
                A[i+1]-=eat-A[i]
            else:
                A[i+1]=0
                A[i]-=eat-A[i]
        elif A[i+1]>=A[i]:
            A[i+1]-=eat
        else:
            A[i]-=eat
        ans+=eat
print(ans)


