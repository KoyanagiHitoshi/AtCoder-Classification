#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
print(N//10*100+min(100,N%10*15))
