#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
a=[int(_) for _ in input().split()]
c=0
while(True):
    for i in range(len(a)):
        if a[i]==0:
            print(c)
            exit()
        elif a[i]%2==0:
            a[i]=a[i]/2
        else:
            print(c)
            exit()
    c+=1
