#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
A=list(map(int,input().split()))
print(*(A[::-2]+A[N%2::2]))
