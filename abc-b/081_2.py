#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
A=list(map(int,input().split()))
c=0
while all(a%2==0 for a in A):
    A=[a/2 for a in A]
    c+=1
print(c)
