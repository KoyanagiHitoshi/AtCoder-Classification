#!/usr/bin/env python
# -*- conding: utf-8 -*-

sx,sy,tx,ty=map(int,input().split())
ans=[]

for i in range(ty-sy):
    ans.append("U")
for i in range(tx-sx):
    ans.append("R")
for i in range(abs(sy-ty)):
    ans.append("D")
for i in range(abs(sx-tx)):
    ans.append("L")

ans.append("L")
for i in range(ty-sy+1):
    ans.append("U")
for i in range(tx-sx+1):
    ans.append("R")
ans.append("D")
ans.append("R")
for i in range(abs(sy-ty)+1):
    ans.append("D")
for i in range(abs(sx-tx)+1):
    ans.append("L")
ans.append("U")

print("".join(ans))
