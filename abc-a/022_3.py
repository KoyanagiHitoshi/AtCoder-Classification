#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,s,t=map(int,input().split())
w=[int(input()) for i in range(n)]
print(sum(s<=sum(w[:i+1])<=t for i in range(n)))
