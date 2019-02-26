#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=input()
T=S[::-1]
flag=0
for i in range(len(S)):
    if S[i]!=T[i] and S[i]!="*" and T[i]!="*":flag=1
print("YES" if flag==0 else "NO")


