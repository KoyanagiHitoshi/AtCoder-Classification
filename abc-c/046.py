#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
t=a=1
for i in range(N):
    T,A=map(int,input().split())
    num=max(-(-t//T),-(-a//A))
    t,a=num*T,num*A
print(t+a)
