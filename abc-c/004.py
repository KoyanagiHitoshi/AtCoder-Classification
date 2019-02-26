#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())%30
X=[1,2,3,4,5,6]
for i in range(N):
    tmp=X[i%5+1]
    X[i%5+1]=X[i%5]
    X[i%5]=tmp
print(*X,sep="")

