#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,A,B=map(int,input().split())
print(A*max(0,N-5)+B*min(N,5))
