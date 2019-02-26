#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.append(X)
y.append(Y)
print("No War" if max(x)<min(y) else "War")
