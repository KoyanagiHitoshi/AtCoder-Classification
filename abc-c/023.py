#!/usr/bin/env python
# -*- conding: utf-8 -*-

R,C,K=map(int,input().split())
N=int(input())
w=[0]*R
h=[0]*C
v=[]
for i in range(N):
    r,c=map(lambda x:int(x)-1,input().split())
    v.append([r,c])
    w[r]+=1
    h[c]+=1
x=[0]*(10**5+1)
y=[0]*(10**5+1)
for t in w:x[t]+=1
for t in h:y[t]+=1
ans=0
for i in range(K+1):
    ans+=x[i]*y[K-i]
for i,j in v:
    b=w[i]+h[j]
    ans+=(b==K+1)-(b==K)
print(ans)
