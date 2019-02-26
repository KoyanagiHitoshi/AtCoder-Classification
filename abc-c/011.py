#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
NG=[int(input()) for i in range(3)]
if N in NG:
    print("NO")
    exit()
for i in range(100):
    N-=3
    if N in NG:
        N+=1
        if N in NG:
            N+=1
            if N in NG:
                print("NO")
                exit()
print("YES" if N<=0 else "NO")
