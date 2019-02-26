#!/usr/bin/env python
# -*- conding: utf-8 -*-

N=int(input())
print("YES" if all([N%n for n in range(2,int(N**.5)+1)]) else "NO")

