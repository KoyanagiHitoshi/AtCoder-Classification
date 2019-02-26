#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
X=list(map(int,input().split()))
S=sorted(X)
b=S[N//2]
a=S[(N//2)-1]
for i in X:
    print(b if i<b else a)
