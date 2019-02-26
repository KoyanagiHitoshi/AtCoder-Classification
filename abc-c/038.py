#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
diff=0
ans=N
for i in range(N-1):
    if A[i]<A[i+1]:
        diff+=1
        ans+=diff
    else:
        diff=0
print(ans)

