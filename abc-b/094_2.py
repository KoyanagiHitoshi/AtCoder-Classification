#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m,x=map(int,input().split())
s=sum(int(_)<x for _ in input().split())
print(min(s,m-s))
