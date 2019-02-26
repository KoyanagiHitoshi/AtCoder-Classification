#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k,x,y=(int(input()) for _ in [0]*4)
print(n*x-(x-y)*max(n-k,0))
