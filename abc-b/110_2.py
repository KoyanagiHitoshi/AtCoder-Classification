#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
print("No War" if max(max(x),X)<min(min(y),Y) else "War")
