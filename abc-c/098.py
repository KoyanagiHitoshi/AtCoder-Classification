#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
S=input()
cnt=S.count("E")
m=cnt
for i in S:
    if i=="E":
        cnt-=1
    else:
        cnt+=1
    m=min(m,cnt)
print(m)
