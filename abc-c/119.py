#!/usr/bin/env python
# -*- conding: utf-8 -*-

from itertools import product
N,*ABC=map(int,input().split())
L=[int(input()) for i in range(N)]
MP=10**9
for P in product([0,1,2,3],repeat=N):
    if {0,1,2}<=set(P):
        m=[0,0,0]
        for p,l in zip(P,L):
            if p!=3:m[p]+=l
        cost1=sum(abs(m-l) for m,l in zip(m,ABC))
        cost2=sum(1 for i in P if i!=3)-3
        MP=min(MP,cost1+cost2*10)
print(MP)
