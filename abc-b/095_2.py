#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,x=map(int,input().split())
l=[int(input()) for _ in range(n)]
print(n+((x-sum(l))//min(l)))
