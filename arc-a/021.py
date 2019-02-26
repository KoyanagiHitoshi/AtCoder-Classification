#!/usr/bin/env python
# -*- conding: utf-8 -*-

A=[list(map(int,input().split())) for i in range(4)]
flag=0
for i in range(4):
    if A[i][0]==A[i][1] or A[i][1]==A[i][2] or A[i][2]==A[i][3]:flag=1
for i in range(4):
    if A[0][i]==A[1][i] or A[1][i]==A[2][i] or A[2][i]==A[3][i]:flag=1
print("CONTINUE" if flag==1 else "GAMEOVER")
