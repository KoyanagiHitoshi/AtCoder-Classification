#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
x,k=1,0
while True:
    x=2*x+1 if (len(str(bin(N)))-k)%2 else 2*x
    if x>N:
        print("Takahashi" if k else "Aoki")
        break
    k^=1
