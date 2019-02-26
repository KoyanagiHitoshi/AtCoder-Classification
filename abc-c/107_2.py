#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
x=sorted(list(map(int,input().split())))
print(min((min(abs(x[i])+abs(x[i+k-1]-x[i]),abs(x[i+k-1])+abs(x[i]-x[i+k-1]))) for i in range(n-k+1)))
