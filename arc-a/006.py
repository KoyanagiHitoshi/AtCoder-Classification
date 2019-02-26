#!/usr/bin/env python
# -*- conding: utf-8 -*-

E=set(input().split())
b=input()
L=set(input().split())
l=len(E&L)
ans=0
if l==5 and b in L:ans=2
elif l==6:ans=1
elif l>2:ans=8-l
else:ans=0
print(ans)
