#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=int(input())
l=[]
while (S not in l):
    l.append(S)
    if S%2==0:S//=2
    else:S=3*S+1
print(len(l)+1)
