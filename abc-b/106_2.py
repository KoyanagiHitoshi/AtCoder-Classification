#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
p=0
for i in range(105,n+1,2):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==8:
        p+=1
print(p)
