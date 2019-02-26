#!/usr/bin/env python
# -*- conding: utf-8 -*-

l,w=map(int,input().split())
n=int(input())
for i in range(n):
    a=int(input())
    print(l-a if l>a else "0" if w>=a else "-1")


