#!/usr/bin/env python
# -*- conding: utf-8 -*-

D=map(int,input().split())
J=map(int,input().split())
print(sum(max(d,j) for d,j in zip(D,J)))
