#!/usr/bin/env python
# -*- conding: utf-8 -*-

A,B,C,X,Y=map(int,input().split())
print(min(A*X+B*Y,C*2*Y+A*max(0,X-Y),C*2*X+B*max(0,Y-X)))
