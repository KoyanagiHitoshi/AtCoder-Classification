#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
l=[input() for _ in range(N)]
if(N!=len(set(l))):
    print("No")
    exit()
for i in range(0,N-1):
    if(l[i][len(l[i])-1]!=l[i+1][0]):
        print("No")
        exit()
print("Yes")
