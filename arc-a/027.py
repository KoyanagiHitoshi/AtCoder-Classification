#!/usr/bin/env python
# -*- conding: utf-8 -*-

N,A,B=map(int,input().split())
if N>5:print(A*(N-5)+B*5)
else:print(B*N)

