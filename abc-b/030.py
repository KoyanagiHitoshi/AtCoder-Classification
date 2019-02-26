#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
a=abs(n%12*30-5.5*m)
print(min(a,360-a))
