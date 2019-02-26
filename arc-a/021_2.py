#!/usr/bin/env python
# -*- conding: utf-8 -*-

A=[list(map(int,input().split())) for i in range(4)]
flag=0
for x in range(4):
    for y in range(3):
        if A[x][y]==A[x][y+1] or A[y][x]==A[y+1][x]:flag=1
print("CONTINUE" if flag==1 else "GAMEOVER")
