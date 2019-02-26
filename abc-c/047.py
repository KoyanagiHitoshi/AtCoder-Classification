#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=input()[::-1]
ans=0
now=S[0]
for i in range(len(S)):
    if S[i]!=now:
        ans+=1
        now=S[i]
print(ans)



