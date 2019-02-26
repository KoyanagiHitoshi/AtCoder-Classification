#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c,x=[int(input()) for _ in range(4)]
print([500*x+100*y+50*z for z in range(c+1) for y in range(b+1) for x in range(a+1)].count(x))
