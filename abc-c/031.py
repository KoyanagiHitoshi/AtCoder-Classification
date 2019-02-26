#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
ans=-3000
for i in range(N):
    a=-3000
    t=0
    for j in range(N):
        if i!=j:
            l,r=sorted([i,j])
            if sum(A[l+1:r+1:2])>a:
                t=j
                a=sum(A[l+1:r+1:2])
    l,r=sorted([i,t])
    ans=max(ans,sum(A[l:r+1:2]))
print(ans)
