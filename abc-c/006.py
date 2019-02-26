#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,M=map(int,input().split())
for x in range(N+1):
    for y in range(N+1):
        z=N-x-y
        if 2*x+3*y+4*z==M and z>=0:
            print(x,y,z)
            exit()
print("-1 -1 -1")
