#!/usr/bin/env python
# -*- conding: utf-8 -*-

def ketasu(N):
    count=1
    while N>=10:
        N//=10
        count+=1
    return count
N=int(input())
keta=10**10
for i in range(1,int(N**.5)+1):
    if N%i==0:
        keta=min(keta,max(ketasu(i),ketasu(N//i)))
print(keta)
        


