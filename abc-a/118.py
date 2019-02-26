#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
print(a+b if b%a==0 else b-a)
