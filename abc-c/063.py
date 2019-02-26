#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
S=sorted([int(input()) for i in range(N)]+[0])
for num,s in enumerate(S):
    ans=sum(S)-s
    if ans%10!=0:
        print(ans)
        exit()
    elif num==N-1:
        print(0)
        exit()
    else:continue
