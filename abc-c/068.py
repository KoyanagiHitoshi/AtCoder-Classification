#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,M=map(int,input().split())
sa=set()
sb=set()
for i in range(M):
    a,b=map(int,input().split())
    if a==1:sb.add(b)
    if b==N:sa.add(a)
print("IMPOSSIBLE" if len(sa&sb)==0 else "POSSIBLE")
